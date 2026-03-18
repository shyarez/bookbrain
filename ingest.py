# ingest.py
import os
from dotenv import load_dotenv

load_dotenv()
if "GEMINI_API_KEY" in os.environ and "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = os.environ["GEMINI_API_KEY"]

from src.ingestion.pdfLoader import load_and_split
from src.rag.retriever import create_vectorstore

DATA_PATH = "data"

all_docs = []

for file in os.listdir(DATA_PATH):
    if file.endswith(".pdf"):
        docs = load_and_split(os.path.join(DATA_PATH, file))
        all_docs.extend(docs)

create_vectorstore(all_docs)

print("Ingestion complete")