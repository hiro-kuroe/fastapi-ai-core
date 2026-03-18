# 🚀 fastapi-ai-core

Production-ready FastAPI backend for AI-powered applications.  
Includes OpenAI integration, usage tracking, and Dockerized deployment.

---

## 🔥 Why This Exists

Most "AI APIs" are just wrappers around OpenAI.

This project is different.

It is designed as a **real backend foundation for monetizable AI services**, including:

- Usage tracking (token-based)
- User-level data handling (extensible)
- Clean service-layer architecture
- Ready for billing integration (Stripe-ready structure)

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
- Service-layer separation (production style)
- Dockerized environment (ready to deploy)

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
      "prompt": "Did Docker setup succeed?"
    }

---

## 🗃️ Usage Logging (Core Feature)

Each request is stored with:

- prompt
- response
- total_tokens
- user_id
- created_at

This enables:

- Cost tracking
- Usage-based billing
- Analytics

---

## 🔐 Authentication (Current State)

Temporary user injection:

    {"id": 1}

Designed for easy upgrade to:

- JWT authentication
- Role-based access
- Multi-tenant usage tracking

---

## 💡 Real-World Use Cases

- SaaS AI backend
- Internal company AI tools
- Chat-based services
- Token-based billing systems

---

## 🚧 Roadmap

- JWT authentication
- Stripe subscription integration
- Token quota enforcement
- Streaming responses (real-time AI)
- RAG (Retrieval-Augmented Generation)

---

## 🧠 Architecture Philosophy

This is not a demo.

This is a **foundation for production AI systems**:

- Clean separation of concerns
- Extendable service layer
- Designed for scaling and monetization

---

## 📄 License

MIT