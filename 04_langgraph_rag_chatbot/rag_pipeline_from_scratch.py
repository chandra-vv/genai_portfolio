# rag_app.py

# ✅ Import necessary libraries
import os
from dotenv import load_dotenv                        # Load environment variables
from PyPDF2 import PdfReader                          # Read PDF files
from langchain.text_splitter import CharacterTextSplitter  # Split text into chunks
from langchain_openai import OpenAIEmbeddings, ChatOpenAI  # Embeddings & LLM
from langchain_community.vectorstores import FAISS         # Vector DB for storing embeddings
from langchain.chains import RetrievalQA                   # LLM + Retriever QA system

# ✅ Load environment variables (.env file should contain OPENAI_API_KEY)
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Function to read all pages of a PDF and extract text
def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# ✅ Function to split long text into smaller chunks
def split_text(text):
    splitter = CharacterTextSplitter(
        separator="\n",          # Split by newline
        chunk_size=1000,         # Max size of each chunk
        chunk_overlap=200        # Overlap between chunks to preserve context
    )
    return splitter.split_text(text)

# ✅ Function to create a FAISS vector store with OpenAI embeddings
def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    return vector_store

# ✅ Build the RAG pipeline using vector store + LLM
def build_rag_pipeline(vector_store):
    llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
    qa_pipeline = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(),
        chain_type="stuff"  # "stuff" = feed all retrieved docs at once
    )
    return qa_pipeline

# ✅ MAIN RAG FLOW

# Step 1: Load PDF
pdf_path = "Atomic habits.pdf"  # Change this to your PDF file name
print("📥 Loading PDF...")
text = load_pdf(pdf_path)

# Step 2: Split into text chunks
print("✂️ Splitting text into chunks...")
chunks = split_text(text)

# Step 3: Embed and store in FAISS
print("📦 Creating vector store...")
vector_store = create_vector_store(chunks)

# Step 4: Create RAG pipeline
print("🧠 Building RAG pipeline...")
rag_pipeline = build_rag_pipeline(vector_store)

# Step 5: Ask questions
while True:
    question = input("\n🔎 Ask a question (or type 'exit' to quit):\n> ")
    if question.lower() == "exit":
        print("👋 Exiting RAG assistant.")
        break

    answer = rag_pipeline.run(question)
    print("\n💡 Answer:\n", answer)
