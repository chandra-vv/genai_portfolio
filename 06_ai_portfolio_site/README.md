# 🌐 AI Portfolio Site – Streamlit + RetrievalQA

This project is an interactive AI portfolio site built using Streamlit and Retrieval-Augmented Generation (RAG).  
It allows users to ask natural-language questions about user background, experience, and projects, and receive accurate, context-aware answers grounded in a curated knowledge source.

The project demonstrates how LLMs, embeddings, and retrieval pipelines can be combined with a lightweight UI to build a practical, user-facing GenAI application.

---

## 🎯 Purpose

- Provide a conversational interface to explore my profile and projects  
- Demonstrate RetrievalQA in a real, non-toy use case  
- Showcase how LLMs can be embedded into simple web applications  
- Serve as a deployable AI portfolio experience  

---

## 🔍 What This Application Does

- Loads content from about.txt  
- Splits the content into semantic chunks  
- Converts chunks into embeddings  
- Stores embeddings in a vector store  
- Uses RetrievalQA to answer user questions  
- Displays responses through an interactive Streamlit UI  

This approach ensures responses are grounded in source content, minimizing hallucinations.

---

## 🧠 How It Works (High-Level Flow)

1. Knowledge is ingested from about.txt  
2. Text is chunked and converted into embeddings  
3. Embeddings are indexed in a vector store  
4. A user submits a question through the Streamlit UI  
5. Relevant chunks are retrieved using similarity search  
6. The LLM generates an answer using retrieved context  
7. The response is rendered in the browser  

---

## 🧩 Architecture Diagram

User  
↓  
Streamlit UI  
↓  
RetrievalQA Pipeline  
→ Load Knowledge (about.txt)  
→ Chunk Text  
→ Generate Embeddings  
→ Vector Store (Similarity Search)  
↓  
LLM (Answer Generation)  
↓  
Final Response Displayed to User  

---

## 🗂️ Project Structure

06_ai_portfolio_site/  
├── app.py – Streamlit application  
├── about.txt – Knowledge base (profile and project details)  
├── requirements.txt – Python dependencies  
└── README.md – Project documentation  

---

## 🚀 How to Run the Application

Install dependencies:

    pip install -r requirements.txt

Configure environment variables:

Create a file named .env in the project directory and add:

    OPENAI_API_KEY=your_openai_api_key

Run the application:

    streamlit run app.py

The application will open automatically in your browser.

---

## 🛠️ Technology Stack

- Python  
- Streamlit  
- LangChain  
- RetrievalQA  
- OpenAI LLMs  
- Embeddings  
- Vector Store  

---

## 📈 Learning Outcomes

This project demonstrates:

- Building a user-facing GenAI application  
- Practical use of Retrieval-Augmented Generation  
- Grounding LLM responses with external knowledge  
- Rapid prototyping using Streamlit  
- Clean separation between UI, retrieval, and generation logic  

---

## 🔮 Possible Enhancements

- Support multiple documents such as PDF or Markdown  
- Add conversational memory  
- Display source citations with answers  
- Improve UI with tabs or sections  
- Deploy to Streamlit Cloud  

---

⭐ This project serves as a clean, practical example of combining RAG pipelines with an interactive UI for real-world usage.
