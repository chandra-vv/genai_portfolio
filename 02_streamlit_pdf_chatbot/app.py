# app.py

import streamlit as st
from utils import extract_text_from_pdf, chunk_text, create_faiss_index, search_index
from openai import OpenAI
from dotenv import load_dotenv
import os

# ✅ Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ Streamlit page setup
st.set_page_config(page_title="📁 Multi-PDF Chatbot", page_icon="📚", layout="wide")
st.title("📁 Chat Across Multiple PDFs")
st.markdown("Upload multiple PDFs and ask questions — GPT will answer using *all* documents.")

# ✅ Sidebar instructions
with st.sidebar:
    st.header("🧾 Instructions")
    st.markdown("""
    1. Upload multiple PDF files  
    2. Wait for processing  
    3. Ask any question  
    4. GPT will search across all PDFs for the best answer
    """)

# ✅ Initialize state
if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "index" not in st.session_state:
    st.session_state.index = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Upload multiple files
uploaded_files = st.file_uploader("📎 Upload one or more PDFs", type=["pdf"], accept_multiple_files=True)

# ✅ Process PDFs only once
if uploaded_files and st.session_state.index is None:
    try:
        all_chunks = []

        for file in uploaded_files:
            text = extract_text_from_pdf(file)  # Extract from each PDF
            chunks = chunk_text(text)          # Chunk the text
            all_chunks.extend(chunks)          # Combine into one list

        st.session_state.chunks = all_chunks
        st.session_state.index, _ = create_faiss_index(all_chunks)
        st.success(f"✅ Processed {len(uploaded_files)} files into {len(all_chunks)} chunks!")

    except Exception as e:
        st.error(f"❌ Failed to process PDFs: {e}")

# ✅ Ask a question
if st.session_state.index is not None:
    question = st.text_input("💬 Ask your question:")

    if question:
        try:
            # Search and get best matching chunk
            matched_chunk = search_index(st.session_state.index, question, st.session_state.chunks)

            # Create GPT prompt
            prompt = f"Context:\n{matched_chunk}\n\nQuestion: {question}\nAnswer:"

            # Get GPT answer
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content.strip()

            # Store chat history
            st.session_state.messages.append(("user", question))
            st.session_state.messages.append(("bot", answer))

        except Exception as e:
            st.error(f"❌ GPT error: {e}")

# ✅ Show chat history
if st.session_state.messages:
    st.subheader("🧠 Chat History")
    for sender, msg in st.session_state.messages:
        if sender == "user":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**GPT:** {msg}")
