# Hybrid RAG with Reranking

A local document question-answering application built with
Python, Streamlit, Ollama, vector search, keyword search,
Reciprocal Rank Fusion (RRF), and cross-encoder reranking.

## Project Status

Day 1: Environment setup and local LLM verification.

The initial application tests communication with a local
Ollama model. PDF ingestion, hybrid retrieval, reranking,
source citations, and evaluation will be added incrementally.

## Planned Features

- PDF text extraction and chunking
- Sentence Transformer embeddings
- FAISS vector search
- BM25 keyword retrieval
- Reciprocal Rank Fusion
- Cross-encoder reranking
- Local LLM answer generation using Ollama
- Answers with document and page citations
- Evaluation against a question-answer benchmark
- Streamlit user interface

## Technology Stack

- Python
- Streamlit
- PyMuPDF
- Sentence Transformers
- FAISS
- BM25
- Ollama
- pytest

## Prerequisites

- Python 3.12 or another supported Python version
- Git
- Ollama for Windows
- A local Ollama model

## Setup

Create and activate a virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1