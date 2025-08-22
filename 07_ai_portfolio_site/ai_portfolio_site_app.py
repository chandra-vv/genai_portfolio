import streamlit as st
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

# ✅ Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(api_key=api_key, temperature=0)

# ✅ Load about.txt manually (NO writing here)
about_path = "about.txt"
if not os.path.exists(about_path):
    raise FileNotFoundError("❌ 'about.txt' is missing. Please add it and try again.")

with open(about_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

print("📄 Loaded text:\n", raw_text)

# ✅ Prepare documents
docs = [Document(page_content=raw_text)]
text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = text_splitter.split_documents(docs)

print("\n📦 Chunks Created:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk.page_content[:80]}...")

# ✅ Vector embeddings
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embedding=embeddings)
retriever = vectorstore.as_retriever()

# ✅ Prompt
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant that answers questions only using the context provided.

If the answer is not in the context, say: "I don't have that information."

Context:
{context}

Question: {question}

Answer:
"""
)

# ✅ QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt_template}
)

# ✅ Streamlit UI
# ✅ Streamlit UI
st.set_page_config(page_title="John GenAI Q&A", layout="wide")
st.title("🧠 John - GenAI Q&A Assistant")

query = st.text_input("Ask me something about John:")

if query:
    response = qa_chain.run(query)
    st.success(response)

    # Debug: show chunks
    with st.expander("🔍 Retrieved Chunks"):
        docs = retriever.get_relevant_documents(query)
        for i, doc in enumerate(docs):
            st.markdown(f"**Chunk {i+1}:**\n{doc.page_content}")

# ✅ Sidebar Navigation / Links / Resume
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/0000000", width=100)

    st.markdown("### 📄 Resume")
    if os.path.exists("resume_1.pdf"):
        with open("resume_1.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download Resume",
                data=pdf_file,
                file_name="John_Resume.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Resume file not found.")

    st.markdown("### 🔗 Connect with John")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com)")
    st.markdown("[💻 GitHub](https://github.com)")

    st.markdown("### 💬 Try Asking:")
    st.info("What GenAI projects has John worked on?\nWhere did John work before?\nWhat cloud platforms has he used?")

