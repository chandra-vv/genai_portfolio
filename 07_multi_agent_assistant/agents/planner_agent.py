"""
multi_agent_assistant/agents/planner_agent.py

Planner Agent:
---------------
This module defines the "planner agent," which takes a complex user question
and breaks it down into smaller, focused sub-questions. These sub-questions
are then processed downstream by other agents (e.g., retriever agents).

Components:
- Loads the OpenAI API key from environment variables.
- Initializes a ChatOpenAI LLM with a structured prompt.
- Uses LangChain's LLMChain to run the planning step.
- Provides `planner_agent()` which returns a clean list of sub-questions.
"""

import os
from typing import List
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# ---------------------------------------------------------------------------
# Load environment variables from .env file (expects OPENAI_API_KEY to be set)
# ---------------------------------------------------------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ---------------------------------------------------------------------------
# Initialize the LLM
# - You can change the model name if desired (e.g., "gpt-4o-mini")
# - Temperature=0 makes output more deterministic (less "creative")
# ---------------------------------------------------------------------------
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key)

# ---------------------------------------------------------------------------
# Define the planner prompt template
# - This instructs the model to split a complex question into 3–5 sub-questions
# - The output is expected as a numbered list
# ---------------------------------------------------------------------------
planner_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a research planner. Break down the following complex question into 
3–5 specific, focused sub-questions.

Question:
{question}

Sub-questions (as a numbered list):
"""
)

# ---------------------------------------------------------------------------
# Wrap the LLM with LangChain's LLMChain for convenience
# ---------------------------------------------------------------------------
planner_chain = LLMChain(llm=llm, prompt=planner_prompt)

# ---------------------------------------------------------------------------
# Planner Agent function
# ---------------------------------------------------------------------------
def planner_agent(question: str) -> List[str]:
    """
    Break down a complex question into smaller sub-questions.

    Args:
        question (str): The user's complex question.

    Returns:
        List[str]: A list of clean, individual sub-questions.
    """
    # Run the LLM chain with the question
    raw_output = planner_chain.run(question)

    # Post-process: split by newlines and clean up numbering/extra characters
    sub_questions = [
        q.strip(" .") for q in raw_output.strip().split("\n") if q.strip()
    ]

    return sub_questions
