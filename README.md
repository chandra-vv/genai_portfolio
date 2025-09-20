
# ✅ Vinay Chandra – Generative AI Projects Portfolio

Welcome to my **Generative AI (GenAI) Projects Portfolio**, where I combine my hands-on experience with **LLM-powered applications**.  
This repository is a structured showcase of projects built during my **step-by-step GenAI learning journey**, progressing from basic LLM demos to advanced **multi-agent assistants**.

---

## 📁 Folder Structure

| Folder                        | Description                                                                     |
|-------------------------------|---------------------------------------------------------------------------------|
| `01_llm_basic/`               | Introduction to LLMs – prompt engineering, completions, and simple Q&A.         |
| `02_pdf_qa_chatbot/`          | PDF chatbot using **embeddings + RetrievalQA**.                                 |
| `03_entity_memory_chatbot/`   | Conversational assistant with **Entity Memory** (remembers names/entities).     |
| `04_langgraph_rag_chatbot/`   | Retrieval-Augmented Generation (RAG) chatbot built with **LangGraph**.          |
| `05_rag_chatbot_with_memory/` | Enhanced RAG chatbot with conversational **memory**.                            |
| `06_ai_portfolio_site/`       | Interactive AI portfolio site built with Streamlit.                             |
| `07_multi_agent_assistant/`   | **Advanced AI Agent assistant** with Planner, Retriever, Controller and Memory nodes via LangGraph, Langchain, Vector DBs and Embedding. |

---

## 🚀 Setup Instructions

### 1️⃣ Clone This Repository
```bash
git clone https://github.com/chandra-vv/genai_portfolio.git
cd genai_portfolio
````

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Your API Key

Create a `.env` file in the root or project folder:

```
OPENAI_API_KEY=your-openai-key
```

### 5️⃣ Run a Project

```bash
cd 07_multi_agent_assistant
streamlit run app.py
```

---

## 🌟 Key Skills Demonstrated

* **LLMs (GPT-3.5, GPT-4)**
* **Prompt Engineering**
* **LangChain & LangGraph**
* **Retrieval-Augmented Generation (RAG)**
* **Vector Stores (FAISS)**
* **Conversational Memory (Entity + Buffer)**
* **Streamlit UI for AI apps**
* **Multi-Agent Workflows**

---

## 👨‍💻 About Me

* **Name:** Vinay Chandra Vudharam
* **LinkedIn:** [vvinaychandra](https://www.linkedin.com/in/vvinaychandra/)
* **GitHub:** [chandra-vv](https://github.com/chandra-vv)

---

## ✔️ Folder Layout Recap

```
01_llm_basic/
    app.py

02_pdf_qa_chatbot/
    app.py

03_entity_memory_chatbot/
    app.py

04_langgraph_rag_chatbot/
    app.py

05_rag_chatbot_with_memory/
    app.py

06_ai_portfolio_site/
    app.py

07_multi_agent_assistant/
    app.py
    graph/
    agents/
    about.txt
```
⭐ If you find this repository helpful, consider giving it a star on GitHub and connecting with me on LinkedIn.

---
