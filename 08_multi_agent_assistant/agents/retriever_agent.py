"""
multi_agent_assistant/agents/retriever_agent.py

Retriever Agent:
----------------
This module defines the "retriever agent," which is responsible for:
1. Loading the knowledge base (about.txt).
2. Splitting it into smaller chunks for vector storage.
3. Creating embeddings and building a FAISS vector store.
4. Performing retrieval-augmented QA using LangChain's RetrievalQA chain.

Workflow:
- Input: A dictionary with a "question" string.
- Output: A generated answer from the knowledge base, powered by an LLM + retriever.
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

# ---------------------------------------------------------------------------
# Load environment variables (expects OPENAI_API_KEY to be present in .env)
# ---------------------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

# ---------------------------------------------------------------------------
# Retriever Agent function
# ---------------------------------------------------------------------------
def retriever_agent(inputs: Dict[str, Any]) -> str:
    """
    Answer a user question by retrieving relevant chunks from the knowledge base.

    Args:
        inputs (Dict[str, Any]): Dictionary containing the user's question.
            Required key: "question" (str)

    Returns:
        str: Generated answer from the retriever + LLM.
    """
    # Initialize the LLM (deterministic outputs with temperature=0)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key)

    # Resolve absolute path for about.txt (knowledge base file)
    file_path = os.path.join(os.path.dirname(__file__), "..", "about.txt")

    # Load and split the documents into manageable chunks
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(documents)

    # Embed the chunks and create a FAISS vector store
    embeddings = OpenAIEmbeddings(api_key=api_key)
    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()

    # Create RetrievalQA chain (retriever + LLM)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False  # set True if you also want sources
    )

    # Run QA chain with the provided question
    question = inputs.get("question", "").strip()
    if not question:
        return "⚠️ No question provided."

    return qa_chain.run(question)
