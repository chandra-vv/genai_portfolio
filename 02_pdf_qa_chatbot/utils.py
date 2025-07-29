# utils.py

# ✅ Import required libraries
import fitz  # PyMuPDF — used to read and extract text from PDF files
import nltk  # Natural Language Toolkit — used for breaking text into sentences
import numpy as np  # Numerical operations, especially useful for vector math
import pickle  # For saving/loading Python objects (optional for advanced use)
import faiss  # Facebook AI Similarity Search — used for fast vector search
import os  # To access environment variables like API keys
from openai import OpenAI  # OpenAI client for accessing embeddings and GPT
from dotenv import load_dotenv  # Loads API keys from a .env file

# ✅ Download NLTK's sentence tokenizer (only needs to be done once)
nltk.download("punkt")

# ✅ Load OpenAI API key securely from your .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔍 Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    """
    Reads a PDF file and extracts text from all pages using PyMuPDF.
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")  # Open the PDF file as a stream
    text = ""
    for page in doc:
        text += page.get_text()  # Extract text from each page
    return text  # Return the full text from the PDF

# ✂️ Function to split text into chunks
def chunk_text(text, chunk_size=5):
    """
    Breaks large text into smaller chunks of N sentences (default 5).
    This makes it easier to embed and search meaningfully.
    """
    sentences = nltk.sent_tokenize(text)  # Break text into individual sentences
    # Group every 5 sentences into one chunk
    chunks = [" ".join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks  # Return the list of chunks

# 🔗 Function to get vector embedding of a given text
def get_embedding(text):
    """
    Converts a chunk of text into a numeric vector using OpenAI's embedding model.
    """
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"  # Lightweight and fast embedding model
    )
    return np.array(response.data[0].embedding)  # Convert response to NumPy array for FAISS

# 🧠 Function to build FAISS index from all chunks
def create_faiss_index(chunks):
    """
    Converts all chunks into vectors and builds a FAISS index for similarity search.
    """
    vectors = [get_embedding(chunk) for chunk in chunks]  # Get embeddings for all chunks
    dim = len(vectors[0])  # Get the dimension of the embedding (e.g., 1536)
    index = faiss.IndexFlatL2(dim)  # Initialize FAISS index using L2 distance
    index.add(np.array(vectors))  # Add all vector embeddings to the index
    return index, vectors  # Return the index and raw vectors (optional)

# 🔍 Function to search relevant chunk from query
def search_index(index, query, chunks, k=1):
    """
    Takes a user question, embeds it, searches FAISS index, and returns the best matching chunk.
    """
    query_vector = get_embedding(query).reshape(1, -1)  # Get embedding for the question
    _, result = index.search(query_vector, k)  # Search top-k similar chunks
    return chunks[result[0][0]]  # Return the most relevant chunk
