from langchain_google_genai import ChatGoogleGenerativeAI
import os

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # or gemini-1.5-pro
        temperature=0,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )