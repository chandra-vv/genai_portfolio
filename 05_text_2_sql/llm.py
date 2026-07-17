import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Groq's API is OpenAI-compatible — just point base_url to Groq's endpoint
client = OpenAI(
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
MODEL = os.getenv("GROK_MODEL", "grok-3")

SYSTEM_PROMPT = """You are an expert MySQL SQL assistant.
Given the database schema and a natural language question, generate a single valid MySQL SELECT query.

Rules:
- Output ONLY the SQL query — no explanation, no markdown fences, no code blocks.
- Use standard MySQL syntax (e.g., LIMIT for row caps, backticks for reserved words).
- Never generate INSERT, UPDATE, DELETE, DROP, TRUNCATE, or any DDL/DML statements.
- If the question cannot be answered from the schema, reply with: ERROR: <reason>
"""


def text_to_sql(question: str, schema: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Schema:\n{schema}\n\nQuestion: {question}",
            },
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


def fix_sql(question: str, schema: str, bad_sql: str, error: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Schema:\n{schema}\n\n"
                    f"Question: {question}\n\n"
                    f"The following MySQL SQL failed:\n{bad_sql}\n\n"
                    f"Error: {error}\n\n"
                    "Please provide a corrected MySQL SQL query."
                ),
            },
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()
