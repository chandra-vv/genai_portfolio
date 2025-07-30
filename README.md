# ✅ Vinay Chandra – GenAI Projects Portfolio

Welcome to my **hands-on GenAI project portfolio**, built as part of my learning journey from foundational LLM use to advanced LangChain and Streamlit-powered applications.

Each project below is practical, ethical, and showcases skills in LangChain, OpenAI, Streamlit, Retrieval-Augmented Generation (RAG), memory management, and more — combined with my background in **Data Engineering**.

---

## 📁 Folder Structure

| Folder                        | Description |
|------------------------------|-------------|
| `01_llm_basic/`              | Basic OpenAI API usage and prompt testing |
| `02_pdf_qa_chatbot/`         | Upload a PDF and ask questions (LangChain RAG + Streamlit) |
| `03_entity_memory_chatbot/`  | Chatbot with `ConversationEntityMemory` to remember facts |
| `04_resume_fit_analyzer/`    | Resume-JD analysis tool with ATS score and ethical evaluation |
| `05_langgraph_rag_chatbot/`  | LangGraph-powered chatbot with multi-step memory and routing |
| `06_rag_chatbot_with_memory/`| Custom prompt RAG chatbot with `ConversationBufferMemory` |
| `07_ai_portfolio_site/`      | Central Streamlit site for showcasing all GenAI apps |

---

## ✅ Setup Instructions

### 1️⃣ Clone This Repository

```bash
git clone https://github.com/vinay-genai/genai-portfolio.git
cd genai-portfolio
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# OR
.venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

Navigate into each folder and install the required packages:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, use:

```bash
pip install langchain langchain-openai streamlit faiss-cpu python-dotenv
```

### 4️⃣ Set Up Your `.env` File

Create a `.env` file in the root or project folder:

```
OPENAI_API_KEY=your-openai-key
```

---

## 🎯 Key Skills Covered

✅ OpenAI GPT-3.5 and GPT-4

✅ LangChain & LangGraph

✅ Retrieval-Augmented Generation (RAG)

✅ Conversation Memory & Entity Tracking

✅ Streamlit Dashboards

✅ Prompt Engineering

✅ Document Parsing & Vector Stores (FAISS)

✅ Ethical GenAI Applications

---

## 🚀 How to Run Each Project

For example:

```bash
cd 02_pdf_qa_chatbot
streamlit run app.py
```
---

## 📢 About Me

* **Name:** Vinay Chandra Vudharam
* **Role:** Data Engineer + GenAI Enthusiast
* **LinkedIn:** [vvinaychandra](https://www.linkedin.com/in/vvinaychandra/)
* **GitHub:** [vinay-genai](https://github.com/chandra-vv)

---

## ✅ Final Notes

These projects reflect my deep dive into practical Generative AI development — combining technical depth with ethical design.

## ✔️ Sample Layout Recap:

```
01_llm_basics/
    first_openai_prompt.py
    README.md

02_pdf_qa_chatbot/
    app.py
    utils.py
    requirements.txt
    README.md

03_entity_memory_chatbot/
    app.py
    README.md
    requirements.txt    

04_resume_fit_analyzer/
    app.py
    match_engine.py
    README.md
    requirements.txt
    
05_langgraph_rag_chatbot/
    rag_pipeline_from_scratch.py
    rag_pipeline_streamlit.py
    README.md

06_rag_chatbot_with_memory/
    app.py
    README.md
    about.txt
    requirements.txt
    
07_ai_portfolio_site/
    ai_portfolio_site_app.py
    about.txt
    README.md

```
⭐ If you find this repository helpful, consider giving it a star on GitHub and connecting with me on LinkedIn.
---
