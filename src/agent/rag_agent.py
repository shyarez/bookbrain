from src.rag.pipeline import get_rag_chain

class RAGAgent:
    def __init__(self):
        self.chain = get_rag_chain()

    def ask(self, query: str):
        result = self.chain({"query": query})
        
        return {
            "answer": result["result"],
            "sources": [doc.metadata for doc in result["source_documents"]]
        }