# app.py

# ✅ Import required modules
import streamlit as st                         # Streamlit for building UI
from match_engine import run_match             # Our LangGraph logic
import os

# ✅ Page title
st.set_page_config(page_title="📄 Resume Matcher", layout="centered")
st.title("📄 AI-Powered Resume Matcher")

st.markdown("Upload your **resume** and a **job description** PDF to see how well they match.")

# ✅ File upload
resume_file = st.file_uploader("Upload Resume PDF", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description PDF", type=["pdf"])

# ✅ Save files locally if uploaded
if resume_file and jd_file:
    with open("resume.pdf", "wb") as f:
        f.write(resume_file.read())
    with open("job_description.pdf", "wb") as f:
        f.write(jd_file.read())

    if st.button("🚀 Match Resume"):
        with st.spinner("Matching in progress..."):
            try:
                report = run_match("resume.pdf", "job_description.pdf")
                st.success("✅ Matching complete!")
                st.markdown("### 📝 Resume Matching Report:")
                st.markdown(report)
            except Exception as e:
                st.error(f"❌ Error: {e}")
