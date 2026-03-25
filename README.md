# 🚀 fastapi-ai-core

FastAPI-based backend for building production-aware AI applications.

This project is not just a thin wrapper around the OpenAI API.  
It is designed as a practical backend foundation with context-controlled responses, streaming support, usage logging, estimated cost calculation, and response time monitoring.

---

## 🔥 Why This Exists

Many AI demos stop at "send prompt, get response."

This project takes a different approach.

It is built as a backend foundation for more realistic usage, where:

- responses should be grounded in known context
- hallucinated answers should be reduced
- request behavior should be observable
- system behavior should remain predictable

---

## ⚙️ Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- Alembic
- OpenAI API
- SQLite
- Docker

---

## 📦 Features

- Synchronous AI responses via `/ai/test`
- Streaming AI responses via `/ai/stream`
- Token usage logging per request
- Estimated cost calculation based on total token usage
- Response time monitoring
- Context-based answering with lightweight DB retrieval
- File upload endpoint for adding context data
- Dockerized local setup

---

## 🧠 Context-Based Answering (Lightweight RAG)

Instead of relying purely on model knowledge, this system:

- retrieves relevant data from a database
- injects that data into the prompt
- restricts the model to answer only from the retrieved context

This helps keep responses more predictable and reduces hallucinated answers.  
It also reduces hallucinations by grounding responses in retrieved internal context.

### Retrieval Behavior

- lightweight keyword-based matching
- simple Japanese query handling
- AND search with OR fallback
- no-context fallback for safer behavior

### Fallback Behavior

If no relevant context is found, the system returns safe fallback responses such as:

    "I don't know."
    "No relevant information found."

---

## 🌊 Streaming Support

The project includes a streaming endpoint for incremental AI output:

- `/ai/stream`

Streaming requests are also tracked in usage logs, including:

- total tokens
- estimated cost
- response time
- endpoint name

This makes the backend more suitable for real AI product behavior, not just one-shot request/response demos.

---

## 🗃️ Usage Logging

Each request can be stored with:

- prompt
- response
- total_tokens
- estimated_cost
- response_time_ms
- endpoint
- user_id
- created_at

This enables:

- cost visibility
- latency monitoring
- endpoint-level observability
- usage analytics
- future billing-oriented extensions

---

## 🧪 Initial Data Setup (Important)

This project uses database-based context retrieval.

If the database is empty, the AI may return:

    "No relevant information found."

To test the system properly, you should insert sample data first.

You can do that by:

- calling the `/seed` endpoint
- uploading text files through `/ai/upload`
- inserting records directly into the database

Example context data:

    FastAPI JWT errors are often caused by SECRET_KEY mismatches.
    JWT validation failures commonly come from signature mismatch or expired tokens.

---

## 📤 File Upload

You can upload text data through:

- `POST /ai/upload`

Uploaded content is stored in the database and becomes part of the retrieval context.

This makes it easy to test FAQ-style or internal knowledge style use cases.

---

## 🐳 Quick Start (Docker)

### 1. Clone

    git clone https://github.com/hiro-kuroe/fastapi-ai-core.git
    cd fastapi-ai-core

### 2. Create .env

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

### 3. Build and Run

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

### Example Response

    {
      "result": "FastAPI JWT errors are often caused by SECRET_KEY mismatches."
    }

---

## 🔐 Authentication (Current State)

The current implementation uses mocked user context for demonstration purposes.

Example:

    {"id": 1}

This is intentionally simple and designed to be extended later into:

- JWT authentication
- role-based access control
- multi-tenant usage tracking

---

## 💡 Use Cases

- internal AI tools
- FAQ systems with grounded answers
- cost-aware AI services
- AI-enabled SaaS backends
- controlled-answer support systems

---

## 🚧 Roadmap

- JWT authentication
- token quota control
- admin-facing usage analytics
- Stripe integration
- vector-based search (embeddings)
- richer retrieval strategies

---

## 🧠 Design Approach

This project prioritizes:

- predictable behavior over flashy responses
- grounded answers over model guessing
- backend observability over black-box AI behavior
- simple architecture that can be extended later

---

## Notes

File upload endpoints depend on `python-multipart`.

Make sure it is included in `requirements.txt`.

---

## 📫 Contact

fastapienne@gmail.com

---

## 📄 License

MIT