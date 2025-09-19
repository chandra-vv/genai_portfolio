# 🧠 Entity Memory Chatbot

This chatbot remembers key entities mentioned during your conversation — like your name, company, or location — and refers back to them naturally. It uses LangChain’s `ConversationEntityMemory` and OpenAI GPT-3.5-turbo.

---

## 💡 Features

- Remembers **entities** like names, places, companies
- Maintains **conversation flow**
- Displays stored entities in real time
- Built using LangChain + OpenAI + Streamlit

---

## 🧠 How It Works

This project uses LangChain's `ConversationEntityMemory`, which extracts entities from your input and stores them as memory for later reference.

---

## 🧪 Tech Stack

- `langchain`
- `openai`
- `streamlit`
- `python-dotenv`

---

## 📸 Example

You: My name is John.
Bot: Nice to meet you, John!

You: I live in New York.
Bot: Got it, you're from New York!


---

## 🚀 Run Locally

```bash
cd 02_entity_memory_chatbot
pip install -r requirements.txt

# Add your OpenAI API key to a .env file
echo "OPENAI_API_KEY=your-key-here" > .env

streamlit run app.py




