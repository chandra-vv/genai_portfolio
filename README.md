<div align="center">

  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&width=600&lines=Generative+AI+Engineering;RAG+%7C+Agents+%7C+LangGraph;Production-Grade+AI+Systems" alt="Typing SVG" />

  <h3>⚡ Production-grade Generative AI portfolio — RAG pipelines, multi-agent systems, LangGraph orchestration, and LLMOps</h3>

  <p>
    <a href="https://www.linkedin.com/in/vvinaychandra/">
      <img src="https://img.shields.io/badge/LinkedIn-vvinaychandra-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
    <a href="https://github.com/chandra-vv">
      <img src="https://img.shields.io/badge/GitHub-chandra--vv-181717?style=for-the-badge&logo=github&logoColor=white" />
    </a>
    <a href="mailto:vinaychandra0305@gmail.com">
      <img src="https://img.shields.io/badge/Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
    </a>
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/LangChain-Latest-1C3C3C?style=flat-square" />
    <img src="https://img.shields.io/badge/LangGraph-Latest-FF6B6B?style=flat-square" />
    <img src="https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai&logoColor=white" />
    <img src="https://img.shields.io/badge/FAISS-VectorStore-009688?style=flat-square" />
    <img src="https://img.shields.io/badge/Streamlit-Latest-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
  </p>

  <p>
    <a href="#-projects">Projects</a> •
    <a href="#-architecture">Architecture</a> •
    <a href="#-tech-stack">Tech Stack</a> •
    <a href="#-getting-started">Getting Started</a> •
    <a href="#-about-me">About Me</a>
  </p>

</div>

---

## 📌 About This Portfolio

A hands-on **Generative AI Engineering portfolio** demonstrating production-grade AI system design — from foundational LLM interactions to enterprise-scale multi-agent pipelines. Each project is built to solve a real-world AI engineering challenge.


---

## 🚀 Projects

| # | Project | Description | Key Tech | Demo |
|---|---------|-------------|----------|------|
| 08 | [**ATS Resume Scanner**](./08_ats_resume_scanner/) | Multi-agent ATS scoring system with RAG pipeline — scores resumes 0-100 with skill matching, gap analysis & suggestions | LangGraph · RAG · FAISS · OpenAI | [▶ View](./08_ats_resume_scanner/) |
| 07 | [**Multi-Agent Assistant**](./07_multi_agent_assistant/) | Advanced agentic system with Planner, Retriever, Controller & Memory nodes for complex multi-step reasoning | LangGraph · LangChain · Agents | [▶ View](./07_multi_agent_assistant/) |
| 06 | [**AI Portfolio Site**](./06_ai_portfolio_site/) | Interactive Streamlit portfolio site for live AI project demonstrations | Streamlit · OpenAI | [▶ View](./06_ai_portfolio_site/) |
| 05 | [**RAG Chatbot with Memory**](./05_rag_chatbot_with_memory/) | Context-aware RAG chatbot combining document retrieval with multi-turn conversational memory | LangChain · FAISS · Memory | [▶ View](./05_rag_chatbot_with_memory/) |
| 04 | [**LangGraph RAG Chatbot**](./04_langgraph_rag_chatbot/) | RAG pipeline modeled as a LangGraph state machine with typed state and controlled transitions | LangGraph · RAG · FAISS | [▶ View](./04_langgraph_rag_chatbot/) |
| 03 | [**Entity Memory Chatbot**](./03_entity_memory_chatbot/) | Conversational assistant that recalls names, organizations & facts across turns | LangChain · Entity Memory | [▶ View](./03_entity_memory_chatbot/) |
| 02 | [**PDF Q&A Chatbot**](./02_pdf_qa_chatbot/) | Document intelligence system for accurate PDF Q&A using embeddings and vector retrieval | LangChain · FAISS · Embeddings | [▶ View](./02_pdf_qa_chatbot/) |
| 01 | [**LLM Basics**](./01_llm_basic/) | Foundational prompt engineering, completions, and structured Q&A workflows | OpenAI API · Prompt Engineering | [▶ View](./01_llm_basic/) |

---

## 🏗️ Architecture

### Flagship Project — ATS Resume Scanner (Project 08)

```
┌──────────────────────────────────────────────────────────────────┐
│                        STREAMLIT UI                              │
│              Resume Upload  ·  JD Input  ·  Results              │
└─────────────────────────┬────────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────────┐
│                    LANGGRAPH PIPELINE                            │
│                                                                  │
│  ┌─────────────────┐                                            │
│  │  RAG Node        │  JD chunks → OpenAI Embeddings → FAISS    │
│  │                  │  → retrieves top-k relevant sections       │
│  └────────┬─────────┘                                           │
│           ▼                                                      │
│  ┌─────────────────┐                                            │
│  │  Scoring Node    │  ATS Score 0–100 · Structured JSON        │
│  └────────┬─────────┘                                           │
│           ▼                                                      │
│  ┌─────────────────┐                                            │
│  │  Skill Match     │  Matched ✅ vs Missing ❌ Skills           │
│  └────────┬─────────┘                                           │
│           ▼                                                      │
│  ┌─────────────────┐                                            │
│  │  Gap Analysis    │  Experience & Qualification Gaps           │
│  └────────┬─────────┘                                           │
│           ▼                                                      │
│  ┌─────────────────┐                                            │
│  │  Suggestions     │  3–5 Actionable Resume Improvements        │
│  └────────┬─────────┘                                           │
│           ▼                                                      │
│       📄 Downloadable Markdown Report                            │
└──────────────────────────────────────────────────────────────────┘
```

### Portfolio Architecture — Progressive Complexity

```
Foundation          Retrieval           Orchestration        Production
─────────           ─────────           ─────────────        ──────────
01_llm_basic   →   02_pdf_qa      →    04_langgraph   →    07_multi_agent
                   03_entity_mem  →    05_rag_memory  →    08_ats_scanner
                                       06_portfolio
```

---

## ✨ Key Features Across Projects

- **RAG Pipelines** — FAISS vector search with OpenAI Embeddings for semantic retrieval
- **LangGraph State Machines** — typed state, explicit nodes, controlled transitions
- **Multi-Agent Orchestration** — Planner, Retriever, Controller, Memory agents
- **Structured LLM Outputs** — JSON-validated responses, no fragile regex parsing
- **Production UI** — Streamlit apps with file upload, real-time results, downloadable reports
- **LLMOps Practices** — prompt engineering, output validation, error handling, API key security

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **LLMs** | ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o%20%7C%20GPT--4o--mini-412991?style=flat-square&logo=openai) |
| **Orchestration** | ![LangGraph](https://img.shields.io/badge/LangGraph-StateGraph-FF6B6B?style=flat-square) ![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=flat-square) |
| **RAG & Vector DB** | ![FAISS](https://img.shields.io/badge/FAISS-VectorStore-009688?style=flat-square) ![Embeddings](https://img.shields.io/badge/OpenAI-Embeddings-412991?style=flat-square) |
| **UI & Deployment** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit) |
| **Language** | ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python) |
| **File Parsing** | ![pdfplumber](https://img.shields.io/badge/pdfplumber-PDF-red?style=flat-square) ![docx2txt](https://img.shields.io/badge/docx2txt-DOCX-blue?style=flat-square) |

</div>

---

## ⚡ Getting Started

**Prerequisites:** Python 3.10+, OpenAI API key

```bash
# 1. Clone the repository
git clone https://github.com/chandra-vv/genai_portfolio.git
cd genai_portfolio

# 2. Navigate to any project
cd 08_ats_resume_scanner

# 3. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up environment
cp .env.example .env
# Add your OpenAI API key to .env

# 6. Run
streamlit run app.py
```

> Each project folder contains its own `README.md` with detailed setup instructions and architecture notes.

---

## 🗺️ Roadmap

- [x] LLM Basics & Prompt Engineering
- [x] PDF Q&A with RAG
- [x] Entity Memory Chatbot
- [x] LangGraph RAG Pipeline
- [x] RAG with Conversational Memory
- [x] AI Portfolio Site
- [x] Multi-Agent Assistant
- [x] ATS Resume Scanner
- [ ] Deploy projects to Streamlit Cloud with live demo links
- [ ] Add LLM Fine-tuning project
- [ ] Add LLMOps monitoring with MLflow
- [ ] Add voice AI / multimodal project

---

## 📁 Repository Structure

```
genai_portfolio/
├── 01_llm_basic/                   # LLM fundamentals
├── 02_pdf_qa_chatbot/              # PDF Q&A with RAG
├── 03_entity_memory_chatbot/       # Entity memory conversations
├── 04_langgraph_rag_chatbot/       # LangGraph RAG pipeline
├── 05_rag_chatbot_with_memory/     # RAG + conversational memory
├── 06_ai_portfolio_site/           # Streamlit portfolio site
├── 07_multi_agent_assistant/       # Multi-agent system
│   ├── app.py
│   ├── graph/
│   └── agents/
├── 08_ats_resume_scanner/          # ATS Resume Scanner ⭐
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   ├── .streamlit/
│   └── screenshots/
└── README.md
```

---

## 👨‍💻 About Me

<div align="center">

**Vinay Chandra Vudharam**

<p>
  <a href="https://www.linkedin.com/in/vvinaychandra/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="mailto:vinaychandra0305@gmail.com">
    <img src="https://img.shields.io/badge/Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://github.com/chandra-vv">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

</div>

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">

⭐ **If you find this portfolio helpful, please give it a star!** ⭐

*It helps others discover this work and supports my job search.*

</div>
