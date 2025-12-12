
# ✅ Generative AI Engineering

This repository is a hands-on **Generative AI Engineering** that demonstrates the progressive design, implementation, and orchestration of LLM-powered systems — starting from basic prompt engineering and culminating in a production-style multi-agent assistant.

The projects are intentionally organized as step-by-step learning modules. Each folder focuses on solving a specific real-world limitation of Large Language Models (LLMs) and introduces the architectural patterns required to overcome it (retrieval, memory, orchestration, and agents).

---

## 🧭 Repository Structure


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

## 📘 Project Overview (Concept → Solution → Outcome)

### 🤖 Multi_agent_assistant — Advanced Multi-Agent System
**🔴 Problem**  : Complex tasks require planning, retrieval, orchestration, and memory — single-chain chatbots are insufficient.

**🟢 Solution**  : A **multi-agent assistant** with clearly separated responsibilities using LangGraph and LangChain.

**🏆 Outcome**  : A scalable, production-style AI assistant capable of complex reasoning and task execution.

**⚙️ How it works**
- 🧠 **Planner** decomposes tasks into steps  
- 🔍 **Retriever** fetches relevant knowledge using embeddings and vector databases  
- 🎛️ **Controller** manages decision flow and tool execution  
- 💾 **Memory** maintains short- and long-term conversational context  
All components are orchestrated through a graph-based workflow.

---

### 🧠💾 Rag_chatbot_with_memory — RAG + Conversational Memory
**🔴 Problem**  : Standard RAG systems struggle with follow-up questions and multi-turn context.

**🟢 Solution**  : This project combines document retrieval with conversational memory.

**🏆 Outcome**  : Context-aware, multi-turn conversations grounded in external knowledge.

**⚙️ How it works**  : Conversation history is stored in memory and merged with retrieved document context before response generation.

---

### 🔗 Langgraph_rag_chatbot — RAG with LangGraph
**🔴 Problem**  : Linear RAG pipelines become hard to debug and scale.

**🟢 Solution**  : This project uses **LangGraph** to model the RAG pipeline as a graph-based workflow.

**🏆 Outcome**  : Cleaner control flow, explicit state management, and production-friendly architecture.

**⚙️ How it works**  : Each step (input, retrieval, generation) is represented as a node in a graph with controlled state transitions.

---

### 🧩 Entity_memory_chatbot — Conversational Assistant with Entity Memory
**🔴 Problem**  : Traditional chatbots forget important details like names, organizations, or entities across turns.

**🟢 Solution**  : This project adds **Entity Memory** so the assistant remembers and reuses key entities.

**🏆 Outcome**  : More natural, consistent, and context-aware conversations.

**⚙️ How it works**  : Entities are extracted from messages, stored in memory, and injected into future prompts to preserve context.

---
### 📄 Pdf_qa_chatbot — PDF Q&A with Embeddings + Retrieval
**🔴 Problem** : LLMs cannot access private documents and may hallucinate answers.

**🟢 Solution**  : A **Retrieval-Augmented Generation (RAG)** pipeline that enables question-answering over PDFs using embeddings.

**🏆 Outcome**  : Accurate, document-grounded answers with reduced hallucination.

**⚙️ How it works**  : PDFs are chunked → embedded → stored in a vector index → relevant chunks are retrieved → the LLM answers using retrieved context.

---

### 🧠 LLM — LLM Fundamentals
**🔴 Problem**  : LLMs can produce inconsistent or vague responses without well-designed prompts and constraints.

**🟢 Solution**  : This project introduces prompt engineering, completions, and simple Q&A workflows to build strong LLM fundamentals.

**🏆 Outcome**  : Reliable, structured, and controlled LLM outputs.

**⚙️ How it works**  : User prompts are sent directly to the model, and iterative prompt refinement is used to improve clarity, format, and correctness.

---


## 🛠️ Tech Stack & Concepts Covered

- 🧠 Large Language Models (LLMs)
- ✍️ Prompt Engineering
- 📐 Embeddings & Vector Databases
- 🔎 Retrieval-Augmented Generation (RAG)
- 🧩 Conversational & Entity Memory
- 🔗 LangChain & LangGraph
- 🤖 Multi-Agent Architectures
- 🎨 Streamlit for AI Applications

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
---

## 👨‍💻 About Me

* **Name:** Vinay Chandra Vudharam
* **LinkedIn:** [vvinaychandra](https://www.linkedin.com/in/vvinaychandra/)
* **GitHub:** [chandra-vv](https://github.com/chandra-vv)

---
⭐ If you find this repository helpful, consider giving it a star on GitHub and connecting with me on LinkedIn.

