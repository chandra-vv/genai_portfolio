# 🧠 LangGraph Multi-Agent Assistant

This project implements an advanced **Multi-Agent AI Assistant** using **LangGraph** and **LangChain**.  
It is designed to handle complex user queries by decomposing them into smaller tasks, retrieving relevant knowledge using embeddings and vector databases, and orchestrating execution through a graph-based workflow.

Unlike single-chain chatbots, this assistant follows an **agentic architecture** that supports planning, retrieval, memory, and intelligent routing. An interactive **Streamlit UI** allows users to experiment with the system and optionally query custom documents.

---

## 🎯 Project Objectives

- Build a production-style multi-agent system using LangGraph
- Demonstrate query planning and task decomposition
- Implement Retrieval-Augmented Generation (RAG)
- Maintain conversation memory and context
- Provide an interactive UI for experimentation and learning

---

## ✨ Key Features

- 🤖 Multi-Agent Architecture orchestrated using LangGraph  
- 🧠 Planner Agent to break complex queries into sub-questions  
- 🔍 Retriever Agent powered by embeddings and FAISS  
- 🎛️ Controller logic to route queries based on complexity  
- 💾 Conversation memory for contextual continuity  
- 📄 Optional document upload for custom knowledge  
- 🎨 Interactive Streamlit interface  
- ⚡ Powered by OpenAI GPT-3.5 Turbo  

---

## 🧩 System Architecture

The assistant is implemented as a **graph-based workflow**, where each node has a clearly defined responsibility.

### Architecture Diagram (Logical Flow)

User  
│  
▼  
Streamlit UI  
│  
▼  
Controller (LangGraph)  
│  
├── If query is SIMPLE  
│       └── Retriever Agent  
│               ├── Embeddings  
│               ├── FAISS Vector Search  
│               └── LLM Response  
│  
└── If query is COMPLEX  
        └── Planner Agent  
                ├── Sub-question 1 ──► Retriever Agent ──► Answer  
                ├── Sub-question 2 ──► Retriever Agent ──► Answer  
                ├── Sub-question N ──► Retriever Agent ──► Answer  
                │  
                └── Aggregate Results  
                        │  
                        ▼  
                  Final LLM Response  

Memory Node  
▲  
│  
Stores conversation context across turns  

---

## 🔄 Execution Flow

1. User submits a query through the Streamlit UI  
2. Controller classifies the query as simple or complex  
3. Planner agent generates sub-questions (for complex queries)  
4. Retriever agent answers using embeddings and FAISS  
5. LangGraph orchestrates looping and state updates  
6. Conversation memory is updated  
7. Final answers are displayed in the UI  

---


### Core Components

- **Planner Agent**  
  Decomposes complex user queries into smaller, focused sub-questions.

- **Retriever Agent**  
  Answers questions using embeddings and FAISS-based vector similarity search.

- **Controller (Graph Logic)**  
  Determines execution flow:
  - Complex queries → Planner → Retriever (loop) → End  
  - Simple queries → Retriever → End  

- **Memory Node**  
  Stores and displays conversation context across turns.

---

## 🔄 Execution Flow

1. User submits a query through the Streamlit UI  
2. Graph classifies the query as simple or complex  
3. Planner agent generates sub-questions (if required)  
4. Retriever agent answers using embeddings + FAISS  
5. LangGraph orchestrates execution and state updates  
6. Conversation memory is updated  
7. Final answers are displayed in the UI  

---

## 🗂️ Project Structure

06_multi_agent_assistant/  
├── agents/  
│   ├── planner_agent.py        ## Generates sub-questions for complex queries  
│   └── retriever_agent.py      ## Retrieves answers using embeddings and FAISS  
│  
├── graph/  
│   └── langgraph_multi_agent.py  # LangGraph workflow and routing logic  
│  
├── about.txt                   # Sample knowledge base (replaceable)  
├── app.py                      # Streamlit UI and entry point  
├── requirements.txt            # Python dependencies  
└── README.md                   # Project documentation  

---

## 📘 Example

**Input Question**

How do embeddings improve Retrieval-Augmented Generation (RAG)?

**Generated Sub-Questions**
- What are embeddings?
- What is Retrieval-Augmented Generation?
- How do embeddings enable semantic search?

**Sample Output**
- Embeddings represent text as numerical vectors capturing semantic meaning.  
- In RAG systems, embeddings enable similarity-based retrieval of relevant documents.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chandra-vv/genai_portfolio.git  
cd genai_portfolio/06_multi_agent_assistant  
```
### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv  
source venv/bin/activate      # macOS / Linux  
venv\\Scripts\\activate       # Windows  
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt  
```

### 4️⃣ Configure Environment Variables

```bash
Create a `.env` file:

OPENAI_API_KEY=your_openai_api_key  
```

### 5️⃣ Run the Application

```bash
streamlit run app.py  
```
---

## 🛠️ Technology Stack

- Python  
- LangChain  
- LangGraph  
- OpenAI (GPT-3.5 Turbo)  
- FAISS (Vector Database)  
- Embeddings  
- Streamlit  
- python-dotenv  

---

## 📈 Learning Outcomes

This project demonstrates:
- Agent-based AI system design
- When to use planning vs direct retrieval
- How to orchestrate workflows using LangGraph
- How to combine RAG with memory
- How to build scalable and explainable GenAI systems

---

## 🔮 Future Enhancements

- Add a summarizer agent for long responses  
- Add scoring or ranking agents  
- Support PDF and CSV document ingestion  
- Improve memory using embedding-based recall  
- Enable parallel planning and retrieval  
- Deploy on Streamlit Cloud  

---

⭐ This project serves as a reference implementation for building **agentic Generative AI systems** using LangGraph.
