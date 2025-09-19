# 🧠 LangGraph Multi-Agent Assistant

This project is a **Streamlit demo** that shows how to combine **LangChain** + **LangGraph** into a simple **multi-agent workflow**:

* **Controller Agent**
  Navigate the user query to the Planner Agent or the Retriever Agent based on the complexity of the question.

* **Planner Agent**
  Breaks down a complex user query into smaller, focused sub-questions.

* **Retriever Agent**
  Answer each sub-question by searching an uploaded text file.

---

## ⚡ Project Structure

```
multi_agent_assistant/
│
├── agents/
│   ├── planner_agent.py          # Planner: splits complex queries into sub-questions
│   └── retriever_agent.py        # Retriever: answers sub-questions using embeddings + FAISS
│
├── graph/
│   └── langgraph_multi_agent.py  # Graph wiring: planner → retriever (loop) → end
│
├── about.txt                     # Knowledge base (This is the sample .txt file for testing. You can use your own .txt file.)
├── app.py                        # Streamlit UI
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🧩 How It Works

1. **User Input**:
   The user types a complex question into the Streamlit UI.

2. **Planner Agent** (`planner_agent.py`):
   Uses an LLM to generate a list of sub-questions.

3. **Retriever Agent** (`retriever_agent.py`):
   Uses embeddings + FAISS vector search to answer each sub-question using `about.txt`.

4. **LangGraph Orchestration** (`langgraph_multi_agent.py`):
   Wires planner → retriever in a loop until all sub-questions are answered.

5. **UI Output** (`app.py`):
   Displays sub-questions and answers.

---

## 📚 Example

**Input question:**

```
How do embeddings help improve RAG pipelines?
```

**Output (sample):**

* **Sub-questions**

  * What are embeddings?
  * What is RAG (Retrieval-Augmented Generation)?
  * How do embeddings support retrieval in RAG?

* **Answers**

  * *Q: What are embeddings?*
    *A: Embeddings are numerical representations of text or data…*

---

## 🛠️ Requirements

See [`requirements.txt`](requirements.txt) for exact package versions.
Core dependencies include:

* `streamlit` – for the UI
* `langchain`, `langgraph` – for workflow orchestration
* `langchain-openai`, `openai` – for LLM access
* `faiss-cpu` – for vector search
* `python-dotenv` – for environment variable management

---

## ✨ Future Improvements

* Cache the FAISS index instead of rebuilding on every request.
* Add source documents display in retriever answers.
* Expand `about.txt` into a richer knowledge base.

---
