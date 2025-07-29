# match_engine.py

# ✅ Import required modules
import os
from dotenv import load_dotenv                   # To load environment variables from .env
from langchain_openai import ChatOpenAI          # OpenAI wrapper for ChatGPT models
from langgraph.graph import StateGraph           # For building LangGraph workflows
from typing import TypedDict                     # For structured state definition
from PyPDF2 import PdfReader                     # For reading text from PDF files

# ✅ Load OpenAI key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Step 1: Define LangGraph state structure
class ResumeMatchState(TypedDict):
    resume: str   # Resume text
    jd: str       # Job description text
    report: str   # Final comparison report

# ✅ Step 2: Load the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key)

# ✅ Step 3: Node function that compares resume and JD
def extract_match(state: ResumeMatchState) -> ResumeMatchState:
    prompt = f"""
You are a resume matching agent.

Here is the job description:
{state["jd"]}

Here is the candidate resume:
{state["resume"]}

Compare the resume to the job description. Identify:
- ✅ Matching skills
- ❌ Missing skills
- 🔍 Relevant experience
- 📊 Overall fitness score out of 100

Respond in structured markdown format.
"""
    response = llm.invoke(prompt)
    return {
        **state,
        "report": response.content
    }

# ✅ Step 4: LangGraph builder
builder = StateGraph(ResumeMatchState)
builder.add_node("extract_match", extract_match)
builder.set_entry_point("extract_match")
app = builder.compile()

# ✅ Step 5: Helper to extract text from PDFs
def extract_text(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# ✅ Step 6: Final method to match resume + JD
def run_match(resume_path: str, jd_path: str) -> str:
    resume_text = extract_text(resume_path)
    jd_text = extract_text(jd_path)
    result = app.invoke({"resume": resume_text, "jd": jd_text})
    return result["report"]
