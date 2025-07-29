# app.py

# ✅ Import required libraries
import os
import streamlit as st  # For building the UI
from PyPDF2 import PdfReader  # To read uploaded PDF files
from langchain_community.embeddings import OpenAIEmbeddings  # For converting text to embeddings
from langchain_openai import ChatOpenAI  # For LLM
from langchain_community.vectorstores import FAISS  # Vector store for similarity search
from langchain.text_splitter import CharacterTextSplitter  # To split PDF text
from dotenv import load_dotenv  # For loading OpenAI key from .env

# ✅ Load OpenAI API key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize the embedding model
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# ✅ Streamlit UI
st.title("📄 Ask Questions from your PDF (RAG-powered)")

# ✅ Upload PDF using Streamlit
pdf = st.file_uploader("Upload a PDF", type="pdf")

# ✅ Input box for questions
query = st.text_input("Ask a question about your PDF")

# ✅ Logic to process PDF and answer the query
if pdf and query:
    # ✅ Extract text from PDF
    pdf_reader = PdfReader(pdf)
    raw_text = ""
    for page in pdf_reader.pages:
        raw_text += page.extract_text()

    # ✅ Split text into small chunks
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_text(raw_text)

    # ✅ Create a FAISS vector store from the PDF text
    vectorstore = FAISS.from_texts(texts, embedding=embeddings)

    # ✅ Search for relevant chunks using the query
    docs = vectorstore.similarity_search(query)

    # ✅ Combine the most relevant chunks as context
    context = "\n\n".join([doc.page_content for doc in docs])

    # ✅ Create a prompt to send to LLM
    prompt = f"""Use the following context from the PDF to answer the question:

    {context}

    Question: {query}
    """

    # ✅ Initialize LLM (GPT-3.5)
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

    # ✅ Generate the answer
    response = llm.invoke(prompt)

    # ✅ Display the answer
    st.markdown("### 📢 Answer:")
    st.write(response.content)
