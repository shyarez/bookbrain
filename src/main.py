from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from src.agent.rag_agent import RAGAgent

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the frontend directory for static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="frontend"), name="static")

agent = RAGAgent()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")

@app.post("/ask")
def ask_question(req: QueryRequest):
    return agent.ask(req.query)