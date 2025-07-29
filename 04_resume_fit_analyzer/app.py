import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import os

# ✅ Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Streamlit Setup
st.set_page_config(page_title="📊 Resume Fit Analyzer", layout="wide")
st.title("📊 Ethical Resume Fit Analyzer ")

# ✅ File Upload
resume_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("📑 Upload Job Description (PDF)", type=["pdf"])

# ✅ Helper to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# ✅ Process uploaded files
if resume_file and jd_file:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    # ✅ LangChain Setup
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    prompt_template = PromptTemplate(
        input_variables=["resume", "jd"],
        template="""
You are an expert resume evaluator.
Given the following resume and job description, perform the following:
1. Give an ATS compatibility score out of 100
2. List any missing or weakly mentioned skills in the resume compared to the job description
3. Provide a short summary (2-3 lines) of how well the resume fits the role.

Resume:
{resume}

Job Description:
{jd}
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt_template)
    with st.spinner("Analyzing resume fit..."):
        result = chain.run(resume=resume_text, jd=jd_text)

    st.subheader("✅ Resume Fit Report")
    st.text_area("💬 Evaluation Result", result, height=300)

    # --- Q&A Chatbot over JD ---
    st.markdown("---")
    st.subheader("🧠 Ask Questions About the Job Description")

    user_question = st.text_input("💬 Your question about the job:")

    if user_question:
        qa_prompt = PromptTemplate(
            input_variables=["jd", "question"],
            template="""
    You are an assistant helping a job applicant understand a job description.

    Job Description:
    {jd}

    Question:
    {question}

    Answer in 2-3 sentences.
    """
        )
        qa_chain = LLMChain(llm=llm, prompt=qa_prompt)
        answer = qa_chain.run(jd=jd_text, question=user_question)
        st.success(answer)

    st.markdown("---")
    st.info("Note: This tool does **not** modify your resume. It only provides insights to help you prepare for applications ethically.")

else:
    st.warning("📂 Please upload both Resume and Job Description PDFs to begin analysis.")
