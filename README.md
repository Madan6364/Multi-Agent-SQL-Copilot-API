## Multi-Agent SQL Copilot API
### Overview

This project is a Multi-Agent SQL Copilot built using FastAPI and Python.
It allows users to ask questions in natural language (English), converts the question into an SQL query, executes it on a SQLite database, and returns the results along with a short analysis.

This project demonstrates how multiple agents can work together to automate data analysis using natural language queries.

#### Example

User Input

{
  "user_query": "show all sales"
}

#### Response

{
  "user_query": "show all sales",
  "sql": "SELECT * FROM sales",
  "result": [
    [1, "Laptop", 1000, "India"],
    [2, "Mobile", 500, "USA"],
    [3, "Tablet", 300, "UK"]
  ],
  "analysis": {
    "summary": "Data analysis completed",
    "rows": 3
  }
}
#### Features
Convert natural language questions into SQL queries
Execute SQL queries on a SQLite database
Return real-time database results
Automatic result analysis
Multi-agent architecture
FastAPI Swagger UI support
#### Project Structure
multi-agent-sql-copilot
│
├── app
│   ├── main.py
│   ├── agents
│   │   ├── sql_generator.py
│   │   ├── validator_agent.py
│   │   └── analyst.py
│   │
│   └── db
│       └── database.py
│
├── create_db.py
├── sales.db
└── requirements.txt
#### How It Works
User asks a question in natural language
SQL Generator Agent converts the question into SQL
Validator Agent checks the query
Database executes the SQL query
Analyst Agent analyzes the result and returns a summary
#### How to Run the Project

Step 1 – Install dependencies

pip install -r requirements.txt

Step 2 – Create database

python create_db.py

Step 3 – Run the API

python -m uvicorn app.main:app --reload

Step 4 – Open Swagger UI

http://127.0.0.1:8000/docs
#### Technologies Used

Python, FastAPI, SQLite, Multi-Agent Architecture, REST API
```

---

