import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate

# ✅ Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Setup LLM
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# ✅ Load and split the document
loader = TextLoader("about.txt")
docs = loader.load()
splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
chunks = splitter.split_documents(docs)

# ✅ Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(chunks, embedding=embeddings)

# ✅ Setup conversational memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
memory = st.session_state.memory

# ✅ Custom Prompt Template
custom_prompt_template = """
You are an AI assistant helping a user by answering questions using both their past conversation and relevant document context.

Use the past chat history to remember personal facts (like name, job, company, etc.).

Chat History:
{chat_history}

Relevant Context:
{context}

User Question:
{question}

Answer:
"""
custom_prompt = PromptTemplate.from_template(custom_prompt_template)

# ✅ Build RAG chain with custom prompt
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": custom_prompt},
    verbose=True
)

# ✅ Streamlit UI setup
st.set_page_config(page_title="RAG + Memory Chatbot", layout="wide")
st.title("📚🧠 RAG Chatbot with Conversational Memory")

user_input = st.text_input("Ask something from the document:")

if user_input:
    response = qa_chain.run(user_input)
    st.markdown(f"🤖 **Answer:** {response}")

# 🧠 Show chat history
with st.expander("🗂️ Chat History"):
    for msg in memory.chat_memory.messages:
        st.write(f"**{msg.type.capitalize()}**: {msg.content}")

# 🔍 Debug memory
with st.expander("🧠 Conversation Memory Debug"):
    st.write("**Chat History:**")
    st.write(memory.chat_memory.messages)

    if hasattr(memory, 'entity_store'):
        st.write("**Entities:**")
        st.json(memory.entity_store)
