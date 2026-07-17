# 📚🧠 RAG Chatbot with Conversational Memory

This project implements a **Retrieval-Augmented Generation (RAG) chatbot** enhanced with **conversational memory**.  
The chatbot answers questions about a document while maintaining context across multiple turns, enabling natural follow-up questions and coherent multi-turn conversations.

The system combines **LLMs, vector-based retrieval, and memory**, demonstrating how document-grounded chatbots can be built for real-world applications using LangChain and Streamlit.

---

## 🎯 Purpose

- Enable question-answering over documents using RAG  
- Preserve conversational context across multiple user turns  
- Demonstrate practical use of **Conversational Memory**  
- Provide a clean UI for testing and debugging chatbot behavior  

---

## ✨ Key Features

- 📄 Query documents using Retrieval-Augmented Generation  
- 🧠 Maintain conversational context across turns  
- 🔍 FAISS-based vector search for efficient retrieval  
- 📝 Custom prompts that combine chat history and retrieved context  
- 🧪 Built-in UI to inspect chat history and memory state  
- 🎨 Interactive Streamlit interface  

---

## 🧠 How the System Works

1. A document is loaded into the application  
2. The document is split into semantic chunks  
3. Chunks are converted into embeddings  
4. Embeddings are stored in a FAISS vector store  
5. User questions are processed through a retrieval pipeline  
6. Retrieved context and conversation history are combined  
7. The LLM generates a response grounded in both context and memory  
8. Responses and memory state are rendered in the UI  

This approach ensures that:
- Answers remain grounded in document content  
- Follow-up questions are correctly understood  
- Context is preserved across the conversation  

---

## 🧩 Architecture Diagram

User  
↓  
Streamlit UI  
↓  
Conversational Retrieval Pipeline  
→ Load Document  
→ Chunk Text  
→ Generate Embeddings  
→ FAISS Vector Store  
→ Retrieve Relevant Context  
→ Combine with Chat History  
↓  
LLM Response Generation  
↓  
Answer Displayed with Memory Context  

---

## 🗂️ Project Structure

06_rag_chatbot_with_memory/  
├── app.py            – Streamlit chatbot application  
├── about.txt         – Sample document / knowledge source  
├── requirements.txt  – Python dependencies  
├── .env              – Environment variables (API key)  
└── README.md         – Project documentation  

---

## 📸 Example Interaction

User: What is this document about?  
Bot: The document describes the organization and its AI initiatives.

User: Who is the founder?  
Bot: Based on the document, the founder is John Smith.

The chatbot correctly uses **conversation history** to interpret follow-up questions.

---

## 🚀 How to Run Locally

Install dependencies:

    pip install -r requirements.txt

Configure environment variables:

Create a `.env` file and add:

    OPENAI_API_KEY=your_openai_api_key

Run the application:

    streamlit run app.py

The Streamlit interface will open in your browser.

---

## 🛠️ Technology Stack

- Python  
- LangChain  
- OpenAI LLMs  
- FAISS (Vector Store)  
- ConversationalRetrievalChain  
- Streamlit  
- PyPDF2  
- python-dotenv  

---

## 📈 Learning Outcomes

This project demonstrates:

- How to build a **RAG-based chatbot with memory**
- Practical use of conversational context in GenAI systems  
- Integration of retrieval, memory, and generation  
- Debugging and inspecting chat memory  
- Building user-facing AI tools with Streamlit  

---

## 🔮 Possible Enhancements

- Support multiple document uploads (PDF, Markdown)  
- Add long-term memory using embeddings  
- Display source citations for answers  
- Improve prompt tuning for complex queries  
- Deploy to Streamlit Cloud  

---

⭐ This project serves as a **clean reference implementation** for building document-aware chatbots with **Retrieval-Augmented Generation and conversational memory**.
