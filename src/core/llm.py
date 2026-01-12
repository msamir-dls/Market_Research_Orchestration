import os
from langchain_groq import ChatGroq

def get_llm():
    if not os.getenv("GROQ_API_KEY"):
        raise EnvironmentError("GROQ_API_KEY not set")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )
