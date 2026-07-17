# 🧠 Entity Memory Chatbot

This project implements an **Entity Memory–enabled chatbot** that remembers key entities mentioned during a conversation — such as names, locations, companies, or roles — and refers back to them naturally in later responses.

Unlike basic chatbots that forget details after each turn, this system demonstrates how **entity-based memory** can be used to maintain conversational continuity and personalization. The chatbot is built using **LangChain**, **OpenAI LLMs**, and an interactive **Streamlit UI**.

---

## 🎯 Purpose

- Demonstrate how **entity memory** works in conversational AI  
- Preserve important user-specific details across turns  
- Improve conversation flow and personalization  
- Provide a simple, inspectable UI to visualize stored entities  

---

## ✨ Key Features

- 🧠 Automatically extracts and remembers entities (names, locations, organizations)  
- 🔁 Refers back to remembered entities in future responses  
- 👀 Displays stored entities in real time for debugging and learning  
- 🎨 Interactive Streamlit interface  
- ⚡ Powered by OpenAI GPT-3.5 Turbo  

---

## 🧠 How the System Works

1. A user sends a message through the Streamlit UI  
2. The LLM processes the input and identifies key entities  
3. Entities are stored using LangChain’s ConversationEntityMemory  
4. Stored entities are injected into subsequent prompts  
5. The chatbot uses this memory to generate context-aware responses  
6. The UI displays both the chatbot response and the current memory state  

This approach enables the chatbot to **remember who the user is and what they mentioned**, resulting in more natural interactions.

---

## 🧩 Architecture Diagram

User  
↓  
Streamlit UI  
↓  
ConversationEntityMemory  
→ Entity Extraction  
→ Entity Storage  
↓  
LLM (GPT-3.5 Turbo)  
↓  
Context-Aware Response  
↓  
Displayed with Current Entity Memory  

---

## 🗂️ Project Structure

01_entity_memory_chatbot/  
├── app.py            – Streamlit chatbot application  
├── requirements.txt  – Python dependencies  
├── .env              – Environment variables (API key)  
└── README.md         – Project documentation  

---

## 📸 Example Interaction

User: My name is John.  
Bot: Nice to meet you, John!

User: I live in New York.  
Bot: Got it — you’re from New York.

User: What do you remember about me?  
Bot: Your name is John and you live in New York.

The chatbot correctly recalls stored **entities** from earlier turns.

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
- ConversationEntityMemory  
- OpenAI LLMs  
- Streamlit  
- python-dotenv  

---

## 📈 Learning Outcomes

This project demonstrates:

- How entity-based memory differs from simple chat history  
- Practical use of **ConversationEntityMemory**  
- Improving conversational AI with personalization  
- Inspecting and debugging memory in real time  
- Building interactive AI applications with Streamlit  

---

## 🔮 Possible Enhancements

- Combine entity memory with document retrieval (RAG)  
- Add long-term memory using embeddings  
- Support multiple users or sessions  
- Improve entity visualization in the UI  
- Deploy to Streamlit Cloud  

---

⭐ This project serves as a **clear, practical example** of how **entity memory** can enhance conversational AI systems.
