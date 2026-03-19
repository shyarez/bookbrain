from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()
print("API KEY:", os.getenv("GEMINI_API_KEY"))
def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

def create_vectorstore(documents):
    embeddings = get_embeddings()
    
    vectordb = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    vectordb.persist()
    return vectordb


def load_vectorstore():
    return Chroma(
        persist_directory="vectorstore",
        embedding_function=get_embeddings()
    )