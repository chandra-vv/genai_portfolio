# 🔁 RAG Pipeline – LangGraph + Streamlit

Implements a basic Retrieval-Augmented Generation pipeline using LangGraph and Streamlit UI.

## 🔍 What It Does
- Loads knowledge base
- Uses vector store to retrieve relevant chunks
- Feeds results to LLM via LangGraph

## 🛠️ How to Run
```bash
# Backend
python rag_pipeline_from_scratch.py

# With UI
streamlit run rag_pipeline_streamlit.py