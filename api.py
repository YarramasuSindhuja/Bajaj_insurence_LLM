import os
# Load your environment variables here if needed (e.g., using dotenv)

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
from document_ingestion.pdf_parser import extract_pdf_clauses
from document_ingestion.docx_parser import extract_docx_clauses
from document_ingestion.email_parser import extract_email_clauses
from retrieval.vector_store import MultiDocVectorStore
from llm.query_parser import parse_query
from llm.decision_maker import make_decision 