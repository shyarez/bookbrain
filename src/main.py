from fastapi import FastAPI
from pydantic import BaseModel
from src.agent.rag_agent import RAGAgent

app = FastAPI()
agent = RAGAgent()

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_question(req: QueryRequest):
    return agent.ask(req.query)