import streamlit as st
import os
import re
import json
import pdfplumber
import docx2txt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional

# ─────────────────────────────────────────────
# ENV & CONFIG
# ─────────────────────────────────────────────
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="ATS Resume Ranker",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Guard: stop early if no API key
if not api_key:
    st.error("❌ **OPENAI_API_KEY not found.** Please add it to your `.env` file and restart.")
    st.code("OPENAI_API_KEY=sk-...")
    st.stop()


# ─────────────────────────────────────────────
# CACHED RESOURCES
# ─────────────────────────────────────────────
@st.cache_resource
def load_llm(model: str = "gpt-4o-mini"):
    return ChatOpenAI(api_key=api_key, model=model, temperature=0.2)


@st.cache_resource
def load_embeddings():
    return OpenAIEmbeddings(api_key=api_key)


# ─────────────────────────────────────────────
# FILE EXTRACTION HELPERS
# ─────────────────────────────────────────────
def extract_text_from_pdf(file) -> str:
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()


def extract_text_from_docx(file) -> str:
    return docx2txt.process(file).strip()


def extract_text(file) -> str:
    name = file.name.lower()
    if name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif name.endswith(".docx"):
        return extract_text_from_docx(file)
    elif name.endswith(".txt"):
        return file.read().decode("utf-8").strip()
    else:
        st.error("Unsupported file format. Use PDF, DOCX, or TXT.")
        return ""


# ─────────────────────────────────────────────
# RAG: Build vector store from JD
# ─────────────────────────────────────────────
def build_jd_vectorstore(jd_text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=80)
    chunks = splitter.split_text(jd_text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    embeddings = load_embeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


def retrieve_relevant_jd_sections(vectorstore, resume_text: str, k: int = 4) -> str:
    results = vectorstore.similarity_search(resume_text[:2000], k=k)
    return "\n\n".join([doc.page_content for doc in results])


# ─────────────────────────────────────────────
# LANGGRAPH STATE
# ─────────────────────────────────────────────
class ATSState(TypedDict):
    resume: str
    jd: str
    relevant_jd: str
    ats_score: Optional[int]
    skill_match: Optional[str]
    gap_analysis: Optional[str]
    suggestions: Optional[str]
    final_verdict: Optional[str]
    error: Optional[str]


# ─────────────────────────────────────────────
# LANGGRAPH NODES
# ─────────────────────────────────────────────
def rag_retrieval_node(state: ATSState) -> ATSState:
    """RAG node: retrieves most relevant JD sections against resume."""
    try:
        vectorstore = build_jd_vectorstore(state["jd"])
        relevant = retrieve_relevant_jd_sections(vectorstore, state["resume"])
        return {**state, "relevant_jd": relevant}
    except Exception as e:
        return {**state, "relevant_jd": state["jd"], "error": str(e)}


def scoring_node(state: ATSState) -> ATSState:
    """Node: scores the resume 0–100 against the JD."""
    llm = load_llm()
    prompt = PromptTemplate(
        input_variables=["resume", "relevant_jd"],
        template="""
You are a strict ATS (Applicant Tracking System) evaluator.

Using the most relevant sections of the Job Description below, score the resume from 0 to 100.

Output ONLY valid JSON in this exact format:
{{
  "score": <integer 0-100>,
  "reasoning": "<2-3 sentence explanation>"
}}

Relevant Job Description Sections:
{relevant_jd}

Resume:
{resume}
"""
    )
    chain = prompt | llm
    try:
        result = chain.invoke({"resume": state["resume"], "relevant_jd": state["relevant_jd"]})
        raw = result.content.strip()
        # Strip markdown code fences if present
        raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("```").strip()
        parsed = json.loads(raw)
        score = max(0, min(100, int(parsed.get("score", 0))))
        reasoning = parsed.get("reasoning", "")
        return {**state, "ats_score": score, "final_verdict": reasoning}
    except Exception as e:
        return {**state, "error": f"Scoring failed: {e}"}


def skill_match_node(state: ATSState) -> ATSState:
    """Node: extracts matched and missing skills."""
    llm = load_llm()
    prompt = PromptTemplate(
        input_variables=["resume", "relevant_jd"],
        template="""
Compare the resume to the job description and extract skills.

Output ONLY valid JSON in this format:
{{
  "matched_skills": ["skill1", "skill2", ...],
  "missing_skills": ["skill1", "skill2", ...]
}}

Job Description:
{relevant_jd}

Resume:
{resume}
"""
    )
    chain = prompt | llm
    try:
        result = chain.invoke({"resume": state["resume"], "relevant_jd": state["relevant_jd"]})
        raw = result.content.strip()
        raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("```").strip()
        parsed = json.loads(raw)
        return {**state, "skill_match": json.dumps(parsed)}
    except Exception as e:
        return {**state, "error": f"Skill match failed: {e}"}


def gap_analysis_node(state: ATSState) -> ATSState:
    """Node: identifies experience/qualification gaps."""
    llm = load_llm()
    prompt = PromptTemplate(
        input_variables=["resume", "relevant_jd"],
        template="""
You are a career advisor. Identify gaps between the resume and job description.

Output ONLY valid JSON in this format:
{{
  "experience_gaps": ["gap1", "gap2", ...],
  "qualification_gaps": ["gap1", "gap2", ...]
}}

Job Description:
{relevant_jd}

Resume:
{resume}
"""
    )
    chain = prompt | llm
    try:
        result = chain.invoke({"resume": state["resume"], "relevant_jd": state["relevant_jd"]})
        raw = result.content.strip()
        raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("```").strip()
        parsed = json.loads(raw)
        return {**state, "gap_analysis": json.dumps(parsed)}
    except Exception as e:
        return {**state, "error": f"Gap analysis failed: {e}"}


def suggestions_node(state: ATSState) -> ATSState:
    """Node: provides actionable improvement suggestions."""
    llm = load_llm()
    prompt = PromptTemplate(
        input_variables=["resume", "relevant_jd", "ats_score"],
        template="""
You are a professional resume coach. The resume scored {ats_score}/100 against this job description.

Give 3–5 specific, actionable suggestions to improve this resume for this role.

Output ONLY valid JSON:
{{
  "suggestions": [
    "suggestion 1",
    "suggestion 2",
    ...
  ]
}}

Job Description:
{relevant_jd}

Resume:
{resume}
"""
    )
    chain = prompt | llm
    try:
        result = chain.invoke({
            "resume": state["resume"],
            "relevant_jd": state["relevant_jd"],
            "ats_score": state.get("ats_score", "N/A")
        })
        raw = result.content.strip()
        raw = re.sub(r"```(?:json)?", "", raw).strip().rstrip("```").strip()
        parsed = json.loads(raw)
        return {**state, "suggestions": json.dumps(parsed)}
    except Exception as e:
        return {**state, "error": f"Suggestions failed: {e}"}


# ─────────────────────────────────────────────
# BUILD LANGGRAPH PIPELINE
# ─────────────────────────────────────────────
@st.cache_resource
def build_graph():
    graph = StateGraph(ATSState)

    graph.add_node("rag_retrieval", rag_retrieval_node)
    graph.add_node("scoring", scoring_node)
    graph.add_node("skill_match", skill_match_node)
    graph.add_node("gap_analysis", gap_analysis_node)
    graph.add_node("suggestions", suggestions_node)

    graph.set_entry_point("rag_retrieval")
    graph.add_edge("rag_retrieval", "scoring")
    graph.add_edge("scoring", "skill_match")
    graph.add_edge("skill_match", "gap_analysis")
    graph.add_edge("gap_analysis", "suggestions")
    graph.add_edge("suggestions", END)

    return graph.compile()


# ─────────────────────────────────────────────
# SCORE COLOR HELPER
# ─────────────────────────────────────────────
# ✅ Fixed (handles None safely)
def score_color(score) -> str:
    if score is None:
        return "⚪"
    if score >= 75:
        return "🟢"
    elif score >= 50:
        return "🟡"
    else:
        return "🔴"

def score_label(score) -> str:
    if score is None:
        return "Score unavailable"
    if score >= 75:
        return "Strong Match"
    elif score >= 50:
        return "Moderate Match"
    else:
        return "Weak Match"

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")
    model_choice = st.selectbox(
        "OpenAI Model",
        ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo"],
        index=0,
        help="gpt-4o-mini is faster and cheaper. gpt-4o gives better analysis."
    )
    st.markdown("---")
    st.markdown("### 📖 How it works")
    st.markdown("""
1. **RAG** retrieves the most relevant JD sections using embeddings
2. **LangGraph** orchestrates 4 analysis nodes in sequence:
   - 🎯 ATS Scoring
   - 🛠️ Skill Matching
   - 🔍 Gap Analysis
   - 💡 Improvement Suggestions
""")
    st.markdown("---")
    st.caption("Built with LangChain · LangGraph · OpenAI · Streamlit")


# ─────────────────────────────────────────────
# MAIN UI
# ─────────────────────────────────────────────
st.title("📊 ATS Resume Scorer")
st.markdown("*Powered by RAG + LangGraph multi-agent pipeline*")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Resume")
    resume_input_type = st.radio("Input method", ["Upload File", "Paste Text"], horizontal=True, key="resume_type")
    resume_text = ""
    if resume_input_type == "Upload File":
        resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"], label_visibility="collapsed")
        if resume_file:
            with st.spinner("Extracting resume text..."):
                resume_text = extract_text(resume_file)
            if resume_text:
                st.success(f"✅ Extracted {len(resume_text.split())} words")
                with st.expander("Preview extracted text"):
                    st.text(resume_text[:1500] + ("..." if len(resume_text) > 1500 else ""))
    else:
        resume_text = st.text_area("Paste your resume here:", height=300, placeholder="Paste full resume text...")

with col2:
    st.subheader("📝 Job Description")
    jd_input_type = st.radio("Input method", ["Paste Text", "Upload File"], horizontal=True, key="jd_type")
    jd_text = ""
    if jd_input_type == "Paste Text":
        jd_text = st.text_area("Paste the job description:", height=300, placeholder="Paste full JD text...")
    else:
        jd_file = st.file_uploader("Upload JD", type=["pdf", "docx", "txt"], label_visibility="collapsed")
        if jd_file:
            with st.spinner("Extracting JD text..."):
                jd_text = extract_text(jd_file)
            if jd_text:
                st.success(f"✅ Extracted {len(jd_text.split())} words")

st.markdown("---")

run_btn = st.button("🚀 Analyze Resume", type="primary", use_container_width=True)

# ─────────────────────────────────────────────
# RUN PIPELINE
# ─────────────────────────────────────────────
if run_btn:
    if not resume_text or not jd_text:
        st.warning("⚠️ Please provide both a resume and a job description.")
        st.stop()

    if len(resume_text.split()) < 20:
        st.warning("⚠️ Resume seems too short. Please check the extracted text.")
        st.stop()

    pipeline = build_graph()

    with st.status("🔄 Running ATS pipeline...", expanded=True) as status:
        st.write("📡 Step 1: RAG — retrieving relevant JD sections...")
        st.write("🎯 Step 2: Scoring resume...")
        st.write("🛠️ Step 3: Skill matching...")
        st.write("🔍 Step 4: Gap analysis...")
        st.write("💡 Step 5: Generating suggestions...")

        initial_state: ATSState = {
            "resume": resume_text,
            "jd": jd_text,
            "relevant_jd": "",
            "ats_score": None,
            "skill_match": None,
            "gap_analysis": None,
            "suggestions": None,
            "final_verdict": None,
            "error": None,
        }

        try:
            final_state = pipeline.invoke(initial_state)
            status.update(label="✅ Analysis complete!", state="complete")
        except Exception as e:
            status.update(label="❌ Pipeline error", state="error")
            st.error(f"Pipeline failed: {e}")
            st.stop()

    if final_state.get("error"):
        st.warning(f"⚠️ Partial error during analysis: {final_state['error']}")

    # ─── RESULTS ───────────────────────────────
    st.markdown("## 📈 Results")

    score = final_state.get("ats_score", 0)

    # ✅ Add this block right after:
    if score is None:
        st.error(
            "❌ Scoring failed — the LLM did not return a valid score. This is usually a JSON parsing issue. Raw pipeline error: " + str(
                final_state.get("error", "Unknown")))
        st.stop()
    verdict = final_state.get("final_verdict", "")

    # Score card
    score_col, label_col = st.columns([1, 3])
    with score_col:
        st.metric(
            label=f"{score_color(score)} ATS Match Score",
            value=f"{score}/100",
            delta=score_label(score)
        )
        st.progress((score or 0) / 100)
    with label_col:
        st.markdown("#### 🧠 Scoring Rationale")
        st.info(verdict if verdict else "No reasoning returned.")

    st.markdown("---")

    # Tabs for details
    tab1, tab2, tab3 = st.tabs(["🛠️ Skill Match", "🔍 Gap Analysis", "💡 Suggestions"])

    with tab1:
        raw_skills = final_state.get("skill_match")
        if raw_skills:
            skills = json.loads(raw_skills)
            s_col1, s_col2 = st.columns(2)
            with s_col1:
                st.markdown("#### ✅ Matched Skills")
                matched = skills.get("matched_skills", [])
                if matched:
                    for s in matched:
                        st.markdown(f"- ✅ {s}")
                else:
                    st.write("None found.")
            with s_col2:
                st.markdown("#### ❌ Missing Skills")
                missing = skills.get("missing_skills", [])
                if missing:
                    for s in missing:
                        st.markdown(f"- ❌ {s}")
                else:
                    st.write("No gaps found!")
        else:
            st.warning("Skill match data unavailable.")

    with tab2:
        raw_gaps = final_state.get("gap_analysis")
        if raw_gaps:
            gaps = json.loads(raw_gaps)
            g_col1, g_col2 = st.columns(2)
            with g_col1:
                st.markdown("#### 📉 Experience Gaps")
                exp_gaps = gaps.get("experience_gaps", [])
                if exp_gaps:
                    for g in exp_gaps:
                        st.markdown(f"- ⚠️ {g}")
                else:
                    st.write("No experience gaps found!")
            with g_col2:
                st.markdown("#### 🎓 Qualification Gaps")
                qual_gaps = gaps.get("qualification_gaps", [])
                if qual_gaps:
                    for g in qual_gaps:
                        st.markdown(f"- ⚠️ {g}")
                else:
                    st.write("No qualification gaps found!")
        else:
            st.warning("Gap analysis data unavailable.")

    with tab3:
        raw_sugg = final_state.get("suggestions")
        if raw_sugg:
            sugg = json.loads(raw_sugg)
            suggestions_list = sugg.get("suggestions", [])
            if suggestions_list:
                for i, s in enumerate(suggestions_list, 1):
                    st.markdown(f"**{i}.** {s}")
            else:
                st.write("No suggestions available.")
        else:
            st.warning("Suggestions data unavailable.")

    # ─── DOWNLOAD REPORT ───────────────────────
    st.markdown("---")
    st.markdown("### 📥 Download Report")

    report_lines = [
        "# ATS Resume Analysis Report",
        f"\n## ATS Score: {score}/100 — {score_label(score)}",
        f"\n### Scoring Rationale\n{verdict}",
    ]

    if raw_skills:
        skills_data = json.loads(raw_skills)
        report_lines.append("\n### Matched Skills")
        for s in skills_data.get("matched_skills", []):
            report_lines.append(f"- ✅ {s}")
        report_lines.append("\n### Missing Skills")
        for s in skills_data.get("missing_skills", []):
            report_lines.append(f"- ❌ {s}")

    if raw_gaps:
        gaps_data = json.loads(raw_gaps)
        report_lines.append("\n### Experience Gaps")
        for g in gaps_data.get("experience_gaps", []):
            report_lines.append(f"- {g}")
        report_lines.append("\n### Qualification Gaps")
        for g in gaps_data.get("qualification_gaps", []):
            report_lines.append(f"- {g}")

    if raw_sugg:
        sugg_data = json.loads(raw_sugg)
        report_lines.append("\n### Improvement Suggestions")
        for i, s in enumerate(sugg_data.get("suggestions", []), 1):
            report_lines.append(f"{i}. {s}")

    report_md = "\n".join(report_lines)
    st.download_button(
        label="📄 Download Report as Markdown",
        data=report_md,
        file_name="ats_report.md",
        mime="text/markdown",
        use_container_width=True
    )