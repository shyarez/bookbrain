# ingest.py
import os
from dotenv import load_dotenv

load_dotenv()
if "GEMINI_API_KEY" in os.environ and "GEMINI_API_KEY" not in os.environ:
    os.environ["GEMINI_API_KEY"] = os.environ["GEMINI_API_KEY"]
print("Env variables loaded");
from src.ingestion.pdfLoader import load_and_split
from src.rag.retriever import create_vectorstore

DATA_PATH = "data"
print("Loading data from", DATA_PATH);
if not os.path.exists(DATA_PATH):
    
    print("No data found in the data directory")
    exit(1)
all_docs = []
files = os.listdir(DATA_PATH)

if not files:
    print("❌ No files found in data directory")
else:
    pdf_found = False

    for file in files:
        if file.endswith(".pdf"):
            pdf_found = True

            file_path = os.path.join(DATA_PATH, file)
            docs = load_and_split(file_path)
            all_docs.extend(docs)

    # ✅ If no PDFs found
    if not pdf_found:
        print("❌ No PDF files found in data directory")
    
create_vectorstore(all_docs)

print("Ingestion complete")