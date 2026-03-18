# 🚀 Multi-Agent SQL Copilot API

An AI-powered API that converts natural language queries into SQL using a multi-agent architecture.
Built with FastAPI, this system demonstrates how multiple agents collaborate to generate, validate, optimize, and analyze SQL queries.

---

## 🔥 Features

* Natural Language → SQL conversion
* Multi-agent pipeline (Generator, Validator, Optimizer, Analyst)
* FastAPI-based REST API
* SQLite database integration
* Docker support

---

## 🛠 Tech Stack

* Python
* FastAPI
* SQLite
* Docker
* LLM (OpenAI / Ollama)

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

```bash
docker build -t multi-agent-sql-copilot .
docker run -p 8000:8000 multi-agent-sql-copilot
```

---

## 📡 API Example

**Request**

```
GET /query?user_query=show all users
```

**Response**

```json
{
  "sql": "SELECT * FROM sales LIMIT 10;",
  "result": [[1, "Laptop", 1000, "India"]],
  "analysis": {
    "summary": "Data analysis completed",
    "rows": 1
  }
}
```

---

## 📂 Structure

```
app/
 ├── agents/
 ├── db/
 ├── config.py
 └── main.py
```

---

