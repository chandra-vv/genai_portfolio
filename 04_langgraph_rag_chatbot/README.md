# 🔁 RAG Pipeline – LangGraph + Streamlit

This project implements a **Retrieval-Augmented Generation (RAG) pipeline** using **LangGraph** for orchestration and **Streamlit** for an interactive user interface.  
It demonstrates how document retrieval and language model generation can be combined using a **graph-based execution flow** instead of linear chains.

The goal of this project is to show how **LangGraph can be used to structure, control, and reason about RAG workflows** in a clear and extensible way.

---

## 🎯 Purpose

- Demonstrate a **from-scratch RAG pipeline**
- Use **LangGraph** to explicitly model retrieval and generation steps
- Show how graph-based orchestration improves clarity and control
- Provide both **CLI-based execution** and an **interactive UI**
- Serve as a foundation for more advanced agentic RAG systems

---

## ✨ Key Features

- 🔍 Document retrieval using vector similarity search  
- 🧠 Language model generation grounded in retrieved context  
- 🔗 Graph-based orchestration using LangGraph  
- 🎛️ Explicit control over pipeline execution flow  
- 🎨 Optional Streamlit UI for interactive querying  
- 🧪 Clear separation of retrieval and generation logic  

---

## 🧠 How the Pipeline Works

1. Knowledge base is loaded into the system  
2. Text is split into semantic chunks  
3. Chunks are converted into embeddings  
4. Embeddings are stored in a vector store  
5. A user query triggers the LangGraph workflow  
6. Relevant chunks are retrieved via similarity search  
7. Retrieved context is passed to the LLM  
8. The LLM generates a grounded response  

This design ensures responses are **context-aware, traceable, and extensible**.

---

## 🧩 Architecture Diagram

User  
↓  
Query Input (CLI or Streamlit UI)  
↓  
LangGraph Workflow  
→ Retrieve Node (Vector Store Search)  
→ Generate Node (LLM with Retrieved Context)  
↓  
Final Answer Returned to User  

---

## 🗂️ Project Structure

04_langgraph_rag_chatbot/  
├── rag_pipeline_from_scratch.py     – Standalone RAG pipeline (no UI)  
├── rag_pipeline_streamlit.py        – Streamlit-based interactive UI  
├── knowledge_base/                  – Source documents / text files  
├── requirements.txt                 – Python dependencies  
└── README.md                        – Project documentation  

---

## 🚀 How to Run the Project

Run the backend pipeline (without UI):

    python rag_pipeline_from_scratch.py

Run the interactive Streamlit UI:

    streamlit run rag_pipeline_streamlit.py

Ensure required environment variables (e.g., OpenAI API key) are configured before running.

---

## 🛠️ Technology Stack

- Python  
- LangGraph  
- LangChain  
- OpenAI LLMs  
- Embeddings  
- Vector Store  
- Streamlit  

---

## 📈 Learning Outcomes

This project demonstrates:

- How to build a **RAG pipeline using LangGraph**
- Differences between **graph-based workflows and linear chains**
- Clear separation of retrieval and generation steps
- Building both **CLI and UI-driven AI applications**
- Foundations for scaling toward agent-based RAG systems

---

## 🔮 Possible Enhancements

- Add conversational memory to the pipeline  
- Introduce conditional routing based on query complexity  
- Support multiple document formats (PDF, Markdown)  
- Add evaluation metrics for retrieval quality  
- Extend the graph with planner or summarizer nodes  

---

⭐ This project serves as a **clean, foundational reference** for building **LangGraph-based RAG pipelines** with optional UI support.
