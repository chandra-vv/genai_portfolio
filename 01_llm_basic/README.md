# 🧠 LLM Basics – OpenAI Prompting

This project is the **starting point of the Generative AI journey**.  
It demonstrates the **most fundamental interaction with a Large Language Model (LLM)** by sending a prompt to OpenAI’s API and receiving a generated response.

The goal of this project is to build a clear understanding of how LLMs are invoked programmatically, how prompts are structured, and how responses are returned — before introducing more advanced concepts such as retrieval, memory, or agents.

---

## 🎯 Purpose

- Learn the basic mechanics of calling an LLM API  
- Understand prompt → response interaction  
- Establish a foundation for more advanced GenAI systems  
- Serve as a minimal, easy-to-understand reference implementation  

---

## 🔍 What This Application Does

- Sends a prompt to OpenAI’s Chat API  
- Receives a response from the language model  
- Prints the generated output to the console  

This project intentionally avoids additional abstractions to keep the focus on **core LLM behavior**.

---

## 🧠 How It Works

1. A prompt is defined in the Python script  
2. The prompt is sent to OpenAI’s API  
3. The language model processes the prompt  
4. A generated response is returned  
5. The response is printed to the console  

This simple flow forms the **base pattern** used in all higher-level GenAI applications.

---

## 🗂️ Project Structure

01_llm_basic/  
├── first_openai_prompt.py   – Basic script to call OpenAI API  
├── requirements.txt         – Python dependencies  
├── .env                     – Environment variables (API key)  
└── README.md                – Project documentation  

---

## 🚀 How to Run the Script

Install dependencies:

    pip install -r requirements.txt

Configure environment variables:

Create a `.env` file and add:

    OPENAI_API_KEY=your_openai_api_key

Run the script:

    python first_openai_prompt.py

The generated response from the LLM will be printed in the console.

---

## 🛠️ Technology Stack

- Python  
- OpenAI LLM API  
- python-dotenv  

---

## 📈 Learning Outcomes

This project demonstrates:

- How to interact with an LLM programmatically  
- The basic prompt–response workflow  
- How API keys and environment variables are managed  
- Foundational concepts used in all GenAI applications  

---

## 🔮 Possible Enhancements

- Add prompt templates  
- Experiment with system and user roles  
- Add temperature and max token controls  
- Capture and log responses  
- Extend to a simple interactive CLI  

---

⭐ This project serves as a **minimal, foundational example** for understanding how Large Language Models are accessed and used in practice.
