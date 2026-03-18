from langchain_community.chains import RetrievalQA
from .retriever import load_vectorstore
from .generator import get_llm

def get_rag_chain():
    vectordb = load_vectorstore()
    retriever = vectordb.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=get_llm(),
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain