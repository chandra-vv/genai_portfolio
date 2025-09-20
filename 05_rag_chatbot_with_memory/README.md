
---

## 📁 `06_rag_chatbot_with_memory/README.md`

```markdown
# 📚🧠 RAG Chatbot with Conversational Memory

This chatbot answers questions about a document using **Retrieval-Augmented Generation (RAG)** and **Conversational Memory**. It combines OpenAI GPT-3.5, LangChain's `ConversationalRetrievalChain`, and Streamlit UI.

---

## 💡 Features

- Upload a document and chat over its content
- Uses **FAISS** vector store for fast retrieval
- Maintains **chat memory** using `ConversationBufferMemory`
- Custom prompt integrates chat history and retrieved context
- Built-in UI to **debug memory and chat logs**

---

## 🧪 Tech Stack

- `langchain`
- `openai`
- `streamlit`
- `PyPDF2`
- `python-dotenv`

---

## 🧠 How It Works

1. Loads a document (currently `about.txt`)
2. Chunks it using `CharacterTextSplitter`
3. Creates embeddings with OpenAI + FAISS vector store
4. Uses `ConversationalRetrievalChain` for chat with memory
5. Renders responses in Streamlit and shows memory state

---

## 📸 Example Interaction

User: What is this document about?
Bot: The document is about our company and its AI initiatives.

User: Who is the founder?
Bot: The document states the founder is John Smith.


---

## 🚀 Run Locally

```bash
cd 06_rag_chatbot_with_memory
pip install -r requirements.txt

# Add your OpenAI API key
echo "OPENAI_API_KEY=your-key-here" > .env

streamlit run app.py
