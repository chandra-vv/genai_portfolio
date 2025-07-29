import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from dotenv import load_dotenv
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

load_dotenv()

# Streamlit setup
st.set_page_config(page_title="🧠 Entity Memory Chatbot")
st.title("🧠 Entity Memory Chatbot")

# Load LLM
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Initialize memory and conversation chain
if "entity_memory" not in st.session_state:
    st.session_state.entity_memory = ConversationEntityMemory(llm=llm)

if "conversation" not in st.session_state:
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=st.session_state.entity_memory,
        prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
        verbose=True,
    )

# User input
user_input = st.text_input("You:", key="input")

if user_input:
    response = st.session_state.conversation.run(user_input)
    st.markdown(f"🤖 Bot: {response}")

# Display stored entities
with st.expander("🧠 Stored Entities"):
    stored = st.session_state.entity_memory.entity_store
    if stored:
        # Inspecting how stored data looks and rendering
        for entity in stored:
            # If entities are stored as a dictionary, you can access keys and values
            if isinstance(entity, dict):
                for k, v in entity.items():
                    st.write(f"**{k}**: {v}")
            else:
                st.write(f"**Entity**: {entity}")
    else:
        st.info("No entities stored yet.")
