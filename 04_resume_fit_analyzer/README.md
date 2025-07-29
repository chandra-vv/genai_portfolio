# 📊 Resume Fit Analyzer (Ethical GenAI Project)

This project analyzes how well your resume aligns with a specific job description — using OpenAI's GPT models — without modifying or generating resumes. It’s designed to give insights, not fake alignment.

---

## ✅ Features

- Upload your **Resume (PDF)** and **Job Description (PDF)**
- Get an **ATS score (0–100)** based on relevance
- See **missing or weakly mentioned skills**
- Receive a concise **fit summary**
- Interact with a **Q&A chatbot** to ask questions about the JD

---

## ⚙️ Tech Stack

- 🧠 OpenAI GPT-3.5 (via LangChain)
- 🦜 LangChain (LLMChain + PromptTemplate)
- 📄 PyPDF2 for PDF parsing
- 🌐 Streamlit for UI
- 🔐 dotenv for environment variable management

---

## 🚫 What It Doesn’t Do

- ❌ Does not modify or rewrite your resume
- ❌ Does not add/remove skills artificially
- ✅ Ethical and recruiter-friendly

---

## 📦 How to Run Locally

```bash
git clone https://github.com/your_username/genai_portfolio.git
cd genai_portfolio/03_resume_fit_analyzer

# Create .env file
echo "OPENAI_API_KEY=your_openai_key_here" > .env

pip install -r requirements.txt

streamlit run app.py
