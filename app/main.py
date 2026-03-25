from fastapi import FastAPI
from pydantic import BaseModel

from app.db.database import get_connection
from app.agents.sql_generator import generate_sql
from app.agents.validator_agent import validate_sql
from app.agents.analyst import analyze_data

app = FastAPI(title="Multi-Agent SQL Copilot")


class Query(BaseModel):
    user_query: str


@app.post("/ask")
def ask_question(query: Query):

    # Step 1: Generate SQL
    sql_query = generate_sql(query.user_query)

    # Step 2: Validate SQL
    if not validate_sql(sql_query):
        return {"error": "Invalid SQL query"}

    # Step 3: Run SQL
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    conn.close()

    # Step 4: Analyze result
    analysis = analyze_data(result)

    return {
        "user_query": query.user_query,
        "sql": sql_query,
        "result": result,
        "analysis": analysis
    }