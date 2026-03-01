# 🚀 Modular RAG System (Retrieval-Augmented Generation)

A fully modular, production-structured Retrieval-Augmented Generation (RAG) backend built with clean architecture principles.

This project implements document ingestion, multiple chunking strategies, embedding generation, vector indexing, similarity-based retrieval, LLM-based response generation, and retrieval benchmarking.

---

# 📌 Project Overview

This system supports:

- 📄 PDF document ingestion
- ✂️ Fixed and Semantic chunking strategies
- 🧠 Embedding generation
- 🗂 Persistent vector storage using Qdrant
- 🔎 Top-K similarity retrieval
- 📊 Retrieval benchmarking and evaluation
- ✨ LLM-based response generation
- ⚙️ Modular and scalable backend design

---

# 🏗️ Project Structure

backend/
└── app/
├── chunking/
├── embeddings/
├── indexing/
├── retrieval/
├── generation/
├── evaluation/
├── vectorstore/
├── utils/
├── config.py
└── main.py

data/
├── documents/
└── queries/


---

# ✅ Implemented Modules

## 1️⃣ Document Loader
- Extracts text from PDF documents
- Prepares content for chunking

Location:

app/utils/loader.py


---

## 2️⃣ Chunking Strategies

### Fixed Chunking
- Splits text into equal-size chunks
- Baseline method

### Semantic Chunking
- Context-aware chunk splitting
- Improves retrieval relevance

Location:

app/chunking/


---

## 3️⃣ Embedding Module
- Converts text chunks into vector embeddings
- Configurable embedding model
- Query embedding support

Location:

app/embeddings/embedder.py


---

## 4️⃣ Vector Store (Qdrant)
- Persistent local storage
- Cosine similarity search
- Separate collections:
  - rag_fixed
  - rag_semantic

Location:

app/vectorstore/qdrant_store.py


---

## 5️⃣ Indexing
- Embeds chunks
- Stores vectors with metadata (payload)
- Handles collection creation

Location:

app/indexing/indexer.py


---

## 6️⃣ Retrieval
- Embeds query
- Performs similarity search
- Returns Top-K relevant chunks

Location:

app/retrieval/retriever.py


---

## 7️⃣ Generation
- Sends retrieved context to LLM
- Produces final answer
- Isolated generation layer

Location:

app/generation/generator.py


---

## 8️⃣ Evaluation & Benchmarking
- Measures ingestion time
- Measures retrieval time
- Noise testing
- Chunking strategy comparison

Location:

app/evaluation/


---

# 🧠 RAG Pipeline Flow

1. Load document
2. Apply chunking strategy
3. Generate embeddings
4. Store vectors in Qdrant
5. Accept user query
6. Embed query
7. Retrieve Top-K similar chunks
8. Send context to LLM
9. Generate final response

---

# ⚙️ Tech Stack

- Python 3.13
- FastAPI
- Qdrant (Local Vector DB)
- Uvicorn
- dotenv
- Configurable Embedding Model
- LLM API integration

---

# 🔐 Environment Setup

Create a `.env` file inside `backend/`:


API_KEY=your_api_key_here


---

# 📦 Installation

Clone the repository:


git clone <your-repo-url>
cd backend


Install dependencies:


pip install -r requirements.txt


---

# ▶️ Running the Server

From inside `backend/`:


uvicorn app.main:app --reload


Server runs at:


http://127.0.0.1:8000


---

# 📊 Running Benchmark

From inside `backend/`:


python -m app.evaluation.benchmark


This evaluates:
- Fixed vs Semantic chunking
- Retrieval speed
- Context quality impact

---

# 🛑 Ignored Files

The following are excluded via `.gitignore`:

- .env
- __pycache__/
- Qdrant storage files
- SQLite databases
- Lock files
- Virtual environments

---

# 🎯 Design Principles

- Modular architecture
- Separation of concerns
- Replaceable components
- Benchmark-driven development
- Production-ready structure
- Persistent vector storage

---

# 📌 Current Status

- ✅ Core RAG pipeline complete
- ✅ Fixed & Semantic chunking implemented
- ✅ Embedding & retrieval working
- ✅ Benchmarking module implemented
- ⬜ Dockerization pending
- ⬜ Cloud deployment pending
- ⬜ CI/CD integration pending

---

# 🚀 Future Enhancements

- Docker containerization
- AWS EC2 deployment
- Hybrid search (BM25 + Vector)
- UI dashboard
- Authentication layer
- Distributed Qdrant setup

---

# 👨‍💻 Purpose

This project demonstrates a structured, benchmark-oriented RAG implementation suitable for real backend systems rather than tutorial-level prototypes.

---
