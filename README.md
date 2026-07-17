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
    <img src="https://img.shields.io/badge/Chroma-VectorStore-FF6600?style=flat-square" />
    <img src="https://img.shields.io/badge/Streamlit-Latest-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/Gradio-Latest-F97316?style=flat-square" />
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

Projects are numbered in order of increasing complexity, from single-purpose LLM apps through retrieval and orchestration to production-grade, evaluated systems.

---

## 🚀 Projects

| # | Project | Description | Key Tech | Demo |
|---|---------|-------------|----------|------|
| 01 | [**Entity Memory Chatbot**](./01_entity_memory_chatbot/) | Conversational assistant that recalls names, organizations & facts across turns | LangChain · Entity Memory | [▶ View](./01_entity_memory_chatbot/) |
| 02 | [**AI Image Generation**](./02_vacation_image_generator/) | Generates pop-art style vacation images from city/location prompts using OpenAI's `gpt-image-1`, with a Gradio UI for interactive use | OpenAI · gpt-image-1 · Gradio | [▶ View](./02_vacation_image_generator/) |
| 03 | [**RAG Chatbot with Memory**](./03_rag_chatbot_with_memory/) | Context-aware RAG chatbot combining document retrieval with multi-turn conversational memory | LangChain · FAISS · Memory | [▶ View](./03_rag_chatbot_with_memory/) |
| 04 | [**LangGraph RAG Chatbot**](./04_langgraph_rag_chatbot/) | RAG pipeline modeled as a LangGraph state machine with typed state and controlled transitions | LangGraph · RAG · FAISS | [▶ View](./04_langgraph_rag_chatbot/) |
| 05 | [**Text-to-SQL Studio**](./05_text_2_sql/) | Natural language to SQL engine — auto-generates, runs & self-fixes SQL queries against a MySQL database using Groq AI | Groq AI · LLaMA 3.3 · MySQL · Streamlit | [▶ View](./05_text_2_sql/) |
| 06 | ⭐ [**Multi-Agent Assistant**](./06_multi_agent_assistant/) | Advanced agentic system with Planner, Retriever, Controller & Memory nodes for complex multi-step reasoning | LangGraph · LangChain · Agents | [▶ View](./06_multi_agent_assistant/) |
| 07 | [**ATS Resume Scanner**](./07_ats_resume_scanner/) | Multi-agent ATS scoring system with RAG pipeline — scores resumes 0-100 with skill matching, gap analysis & suggestions | LangGraph · RAG · FAISS · OpenAI | [▶ View](./07_ats_resume_scanner/) |
| 08 | ⭐ [**Meeting Minutes Voice Assistant**](./08_meeting_minutes_voice_assistant/) | Transcribes a meeting recording with HF Whisper and generates structured minutes — summary, discussion points, action items — with OpenAI | Hugging Face · Whisper · OpenAI · tenacity | [▶ View](./08_meeting_minutes_voice_assistant/) |
| 09 | ⭐ [**Insurellm Expert Assistant**](./09_insurellm_expert_assistant/) | Production-grade RAG assistant with LLM-based document chunking, dual-query retrieval + reranking, and an automated evaluation dashboard — 4.48/5 answer accuracy across 150 test questions | OpenAI · litellm · Chroma · Gradio · RAG | [▶ View](./09_insurellm_expert_assistant/) |

---

## 🏗️ Architecture

### 🥇 Flagship Project — Insurellm Expert Assistant (Project 09)

```
┌──────────────────────────────────────────────────────────────────┐
│                         INGESTION (offline)                      │
│                                                                    │
│   knowledge-base/*.md ──▶ LLM Chunking ──▶ text-embedding-3-large │
│                          (gpt-4.1-mini)         │                 │
│                                                  ▼                 │
│                                     Chroma Vector Store            │
└──────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────┐
│                      ANSWERING (per question)                    │
│                                                                    │
│  Question ──▶ Query Rewrite ──▶ Retrieve (original + rewritten)  │
│                                          │                         │
│                                          ▼                         │
│                              Merge + LLM Rerank (top 10)          │
│                                          │                         │
│                                          ▼                         │
│                          Grounded Answer Generation                │
└──────────────────────────────────────────────────────────────────┘
                                    │
                        ┌───────────┴───────────┐
                        ▼                       ▼
                 Gradio Chat UI        Evaluation Dashboard
                                    150 test questions · 7 categories
                                    MRR · nDCG · accuracy · completeness
```

### 🥈 Flagship Project — Multi-Agent Assistant (Project 06)

Planner, Retriever, Controller, and Memory agents coordinated via a LangGraph state machine for
complex, multi-step reasoning tasks. See [06_multi_agent_assistant](./06_multi_agent_assistant/)
for details.

### 🥉 Flagship Project — Meeting Minutes Voice Assistant (Project 08)

Transcribes meeting audio with Hugging Face Whisper, then generates structured minutes — summary,
discussion points, action items — with OpenAI. See
[08_meeting_minutes_voice_assistant](./08_meeting_minutes_voice_assistant/) for details.

### Portfolio Architecture — Progressive Complexity

```
Foundation              Retrieval          Orchestration         Production
───────────             ─────────          ─────────────         ──────────
01_entity_memory   →                                         →   06_multi_agent
02_vacation_image       03_rag_memory  →   04_langgraph      →   07_ats_scanner
                                            05_text2sql       →   08_meeting_minutes
                                                               →   09_insurellm_expert_assistant
```

---

## ✨ Key Features Across Projects

- **RAG Pipelines** — FAISS/Chroma vector search with OpenAI Embeddings for semantic retrieval
- **LangGraph State Machines** — typed state, explicit nodes, controlled transitions
- **Multi-Agent Orchestration** — Planner, Retriever, Controller, Memory agents
- **Structured LLM Outputs** — JSON-validated responses, no fragile regex parsing
- **Production UI** — Streamlit/Gradio apps with file upload, real-time results, downloadable reports
- **Automated Evaluation** — retrieval and answer-quality scoring (MRR, nDCG, LLM-as-a-judge) against curated test sets
- **LLMOps Practices** — prompt engineering, output validation, error handling, API key security

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technologies |
|----------|-------------|
| **LLMs** | ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o%20%7C%20GPT--4o--mini-412991?style=flat-square&logo=openai) |
| **Orchestration** | ![LangGraph](https://img.shields.io/badge/LangGraph-StateGraph-FF6B6B?style=flat-square) ![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=flat-square) ![litellm](https://img.shields.io/badge/litellm-Multi--Provider-6C63FF?style=flat-square) |
| **RAG & Vector DB** | ![FAISS](https://img.shields.io/badge/FAISS-VectorStore-009688?style=flat-square) ![Chroma](https://img.shields.io/badge/Chroma-VectorStore-FF6600?style=flat-square) ![Embeddings](https://img.shields.io/badge/OpenAI-Embeddings-412991?style=flat-square) |
| **UI & Deployment** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit) ![Gradio](https://img.shields.io/badge/Gradio-Latest-F97316?style=flat-square) |
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
cd 09_insurellm_expert_assistant

# 3. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up environment
cp .env.example .env
# Add your OpenAI API key to .env

# 6. Run (see each project's own README for its exact run command —
#    e.g. `python app.py` for Gradio projects, `streamlit run app.py` for Streamlit ones)
python app.py
```

> Each project folder contains its own `README.md` with detailed setup instructions and architecture notes.

---

## 🗺️ Roadmap

- [x] Entity Memory Chatbot
- [x] AI Image Generation
- [x] RAG with Conversational Memory
- [x] LangGraph RAG Pipeline
- [x] Text-to-SQL Studio
- [x] Multi-Agent Assistant
- [x] ATS Resume Scanner
- [x] Add voice AI / multimodal project
- [x] Add production RAG system with automated evaluation dashboard (Insurellm Expert Assistant)
- [ ] Deploy projects to Streamlit Cloud with live demo links
- [ ] Add LLM Fine-tuning project
- [ ] Add LLMOps monitoring with MLflow

---

## 📁 Repository Structure

```
genai_portfolio/
├── 01_entity_memory_chatbot/       # Entity memory conversations
├── 02_vacation_image_generator/    # AI image generation
├── 03_rag_chatbot_with_memory/     # RAG + conversational memory
├── 04_langgraph_rag_chatbot/       # LangGraph RAG pipeline
├── 05_text_2_sql/                  # Text-to-SQL Studio
│   ├── app.py
│   ├── db.py
│   ├── llm.py
│   ├── requirements.txt
│   └── .env.example
├── 06_multi_agent_assistant/       # Multi-agent system ⭐
│   ├── app.py
│   ├── graph/
│   └── agents/
├── 07_ats_resume_scanner/          # ATS Resume Scanner
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   ├── .streamlit/
│   └── screenshots/
├── 08_meeting_minutes_voice_assistant/  # Meeting Minutes Voice Assistant ⭐
│   ├── pipeline.py
│   ├── requirements.txt
│   ├── README.md
│   ├── .env.example
│   └── tests/
├── 09_insurellm_expert_assistant/  # Insurellm Expert Assistant ⭐ (flagship)
│   ├── app.py                        # Gradio chat UI
│   ├── evaluator.py                  # Gradio evaluation dashboard
│   ├── implementation/               # ingest.py, answer.py (RAG pipeline)
│   ├── evaluation/                   # eval.py, test.py, tests.jsonl (150 questions)
│   ├── knowledge-base/                # source documents
│   ├── screenshots/
│   ├── requirements.txt
│   ├── README.md
│   └── .env.example
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
