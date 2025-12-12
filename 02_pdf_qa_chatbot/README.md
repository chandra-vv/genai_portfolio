# 📄 PDF Chatbot – Streamlit + LangChain

This project implements a **PDF-based chatbot** that allows users to ask natural-language questions about the contents of a PDF document.  
The chatbot uses **Retrieval-Augmented Generation (RAG)** to ensure answers are grounded in the uploaded PDF, rather than relying on the language model’s general knowledge.

The application combines **LangChain**, **embeddings**, **vector search**, and a **Streamlit UI** to demonstrate how document-aware chatbots can be built for real-world use cases.

---

## 🎯 Purpose

- Enable question-answering over PDF documents  
- Demonstrate document ingestion and semantic search  
- Reduce hallucinations by grounding answers in source text  
- Provide an interactive UI for exploring document content  

---

## ✨ Key Features

- 📄 Upload and query PDF documents  
- 🔍 Semantic retrieval using embeddings and FAISS  
- 🧠 LLM-based answer generation grounded in retrieved context  
- 🎨 Interactive Streamlit interface  
- ⚡ Powered by OpenAI GPT models  

---

## 🧠 How the System Works

1. A PDF document is loaded into the application  
2. Text is extracted from the PDF  
3. The extracted text is split into semantic chunks  
4. Each chunk is converted into an embedding  
5. Embeddings are stored in a FAISS vector store  
6. A user submits a question through the UI  
7. Relevant chunks are retrieved using similarity search  
8. The LLM generates an answer using the retrieved context  
9. The response is displayed in the Streamlit interface  

This pipeline ensures that answers remain **accurate, explainable, and document-grounded**.

---

## 🧩 Architecture Diagram

User  
↓  
Streamlit UI  
↓  
PDF Loader  
→ Text Extraction  
→ Chunking  
→ Embedding Generation  
→ FAISS Vector Store  
↓  
Similarity-Based Retrieval  
↓  
LLM (Answer Generation)  
↓  
Final Answer Displayed to User  

---

## 🗂️ Project Structure

02_pdf_qa_chatbot/  
├── app.py            – Streamlit PDF chatbot application  
├── requirements.txt  – Python dependencies  
├── .env              – Environment variables (API key)  
└── README.md         – Project documentation  

---

## 🚀 How to Run the Application

Install dependencies:

    pip install -r requirements.txt

Configure environment variables:

Create a `.env` file and add:

    OPENAI_API_KEY=your_openai_api_key

Run the application:

    streamlit run app.py

The Streamlit app will open in your browser, allowing you to upload a PDF and start querying it.

---

## 🛠️ Technology Stack

- Python  
- LangChain  
- OpenAI LLMs  
- Embeddings  
- FAISS (Vector Store)  
- Streamlit  
- python-dotenv  

---

## 📈 Learning Outcomes

This project demonstrates:

- How to build a **PDF-based RAG chatbot**
- End-to-end document ingestion and retrieval
- Using embeddings for semantic search
- Grounding LLM responses in external documents
- Building interactive AI applications with Streamlit

---

## 🔮 Possible Enhancements

- Support multiple PDF uploads  
- Add source citations for answers  
- Enable conversational memory  
- Improve chunking strategies for large PDFs  
- Deploy to Streamlit Cloud  

---

⭐ This project serves as a **clean, practical example** of building **PDF-powered chatbots** using Retrieval-Augmented Generation.
