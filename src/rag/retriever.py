from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
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