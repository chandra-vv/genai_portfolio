import streamlit as st
import os
import base64
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from fpdf import FPDF
import re

# ✅ Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=api_key, temperature=0.3)

# ✅ Streamlit UI Config
st.set_page_config(page_title="📄 Final Resume Optimizer", layout="wide")
st.title("📄 All-in-One Resume Optimizer")

# ✅ Inputs
resume_text = st.text_area("📄 Paste Your Resume", height=250)
jd_text = st.text_area("📝 Paste Job Description", height=250)

# ✅ Prompt Templates

keyword_prompt = PromptTemplate(
    input_variables=["jd"],
    template="""
Extract 15–20 important keywords from this job description:

{jd}

Return as comma-separated list only.
"""
)

score_prompt = PromptTemplate(
    input_variables=["resume", "jd"],
    template="""
Evaluate resume relevance to the job description.

Return in this exact format:

Score: XX
Explanation: Short 2–3 sentences.

Resume:
{resume}

Job Description:
{jd}
"""
)

cover_letter_prompt = PromptTemplate(
    input_variables=["resume", "jd"],
    template="""
Write a short professional cover letter based on:

Resume:
{resume}

Job Description:
{jd}

End it with "Sincerely, John".
"""
)

# ✅ Chains
keyword_chain = LLMChain(llm=llm, prompt=keyword_prompt)
score_chain = LLMChain(llm=llm, prompt=score_prompt)
cover_chain = LLMChain(llm=llm, prompt=cover_letter_prompt)

# ✅ PDF Export Helper
def export_pdf(content: str) -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split("\n"):
        pdf.multi_cell(0, 10, line)
    return pdf.output(dest="S").encode("latin1")

# ✅ Button Logic
if st.button("🚀 Optimize My Resume"):
    if not resume_text or not jd_text:
        st.warning("Please provide both resume and job description.")
    else:
        with st.spinner("Running LLM tasks..."):
            keywords_raw = keyword_chain.run({"jd": jd_text})
            keyword_list = [k.strip() for k in keywords_raw.split(",") if k.strip()]

            present = [k for k in keyword_list if k.lower() in resume_text.lower()]
            missing = [k for k in keyword_list if k.lower() not in resume_text.lower()]

            score_result = score_chain.run({"resume": resume_text, "jd": jd_text})
            cover_letter = cover_chain.run({"resume": resume_text, "jd": jd_text})

        # ✅ Score Parsing
        score_match = re.search(r"Score:\s*(\d+)", score_result)
        explanation_match = re.search(r"Explanation:\s*(.*)", score_result, re.DOTALL)

        score = score_match.group(1) if score_match else "N/A"
        explanation = explanation_match.group(1).strip() if explanation_match else "N/A"

        # ✅ Display Results
        st.subheader("✅ Keyword Matching")
        st.success(f"Present Keywords: {', '.join(present)}")
        st.error(f"Missing Keywords: {', '.join(missing)}")

        st.subheader("📈 Relevance Score")
        st.success(f"{score}/100")
        st.info(explanation)

        st.subheader("📬 Cover Letter")
        st.text_area("Generated Cover Letter", cover_letter, height=250)

        # ✅ PDF Export Options
        final_report = f"""
Resume Optimization Report

Score: {score}/100

Explanation:
{explanation}

Present Keywords:
{', '.join(present)}

Missing Keywords:
{', '.join(missing)}

Cover Letter:
{cover_letter}
        """
        pdf_bytes = export_pdf(final_report)
        b64 = base64.b64encode(pdf_bytes).decode()
        st.markdown(f'<a href="data:application/pdf;base64,{b64}" download="Resume_Optimizer_Report.pdf">📥 Download Report as PDF</a>', unsafe_allow_html=True)

# ✅ Sidebar
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/0000000", width=100)
    st.markdown("Made with GPT-4 + LangChain + Streamlit")
    st.markdown("[John’s LinkedIn](https://www.linkedin.com)")
    st.markdown("[GitHub](https://github.com)")
