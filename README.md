# 🚀 fastapi-ai-core

FastAPI-based backend for building AI-powered applications.

This project focuses on **reliable backend behavior**, not just calling an AI API.

---

## 🔥 Why This Exists

Most "AI APIs" are simple wrappers around OpenAI.

This project takes a different approach.

It is built as a **backend foundation for real-world usage**, where:

- Responses must be explainable
- Incorrect answers must be avoided
- System behavior must be predictable

---

## ⚙️ Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- Alembic
- OpenAI API
- Docker

---

## 📦 Features

- AI text generation via OpenAI
- Token usage logging (per request)
- Database persistence (SQLite)
- Service-layer separation
- Dockerized environment

---

## 🧠 Context-Based Answering (Lightweight RAG)

Instead of relying on model knowledge, this system:

- Retrieves relevant data from a database
- Injects it into the prompt
- Forces the model to answer **only from that context**

### Key behaviors

- Japanese query handling (simple tokenization + stop-word removal)
- AND search with OR fallback
- No-context fallback:
  
      "I don't know"
      "No relevant information found."

This avoids hallucinated answers and keeps responses grounded.

---

## 🐳 Quick Start (Docker)

### 1. Clone

    git clone https://github.com/hiro-kuroe/fastapi-ai-core.git
    cd fastapi-ai-core

### 2. Create .env

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

### 3. Build & Run

    docker build -t fastapi-ai-core .
    docker run -p 8000:8000 --env-file .env fastapi-ai-core

---

## 🌐 API Docs

    http://localhost:8000/docs

---

## 🧪 Example Request

### POST /ai/test

    {
      "prompt": "Why does FastAPI JWT fail?"
    }

### Natural Language Input

    "あのさ、FastAPIのJWTのエラーってなんで起きるの？"

→ The system extracts keywords and returns an answer based on stored data.

---

## 🧪 Initial Data Setup (Important)

This project uses DB-based context retrieval.

If the database is empty, the AI will return:

    "No relevant information found."

To test the system, you need to insert sample data.

Example:

    FastAPI JWT エラーは9割SECRET_KEYが原因

You can add data via API or directly in the database.

---

## 🗃️ Usage Logging

Each request is stored with:

- prompt
- response
- total_tokens
- user_id
- created_at

This enables:

- Cost tracking
- Usage-based billing
- Basic analytics

---

## 🔐 Authentication (Current State)

Temporary user injection:

    {"id": 1}

Designed to be extended to:

- JWT authentication
- Role-based access
- Multi-tenant usage tracking

---

## 💡 Use Cases

- Internal AI tools
- FAQ systems with controlled answers
- SaaS AI backends
- Cost-aware AI services

---

## 🚧 Roadmap

- JWT authentication
- Stripe integration
- Token quota control
- Streaming responses
- Vector-based search (embeddings)

---

## 🧠 Design Approach

This project prioritizes:

- Predictable behavior over "smart" responses
- Search reliability over model guessing
- Simple architecture that can be extended later

---

## 📫 Contact

fastapienne@gmail.com

---

## 📄 License

MIT