from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.agents.sql_generator import generate_sql
from app.agents.validator_agent import validate_sql
from app.agents.optimizer_agent import optimize_sql
from app.agents.schema_guard import check_schema
from app.agents.analyst import analyze_data
from app.db.database import run_query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SCHEMA = """
Table: sales(id, product, revenue, region)
"""

@app.get("/query")   # ✅ use GET for testing in browser
def process_query(user_query: str):
    try:
        print("User Query:", user_query)

        # Step 1: Generate SQL
        sql = generate_sql(user_query)
        print("Generated SQL:", sql)

        # Step 2: Schema check (NEW)
        schema_check = check_schema(sql, SCHEMA)
        print("Schema Check:", schema_check)

        if "❌" in schema_check:
            return {"error": schema_check}

        # Step 3: Validate
        validation = validate_sql(sql)
        print("Validation:", validation)

        if "❌" in validation:
            return {"error": validation}

        # Step 4: Optimize
        optimized_sql = optimize_sql(sql)
        print("Optimized SQL:", optimized_sql)

        # Step 5: Run query
        result = run_query(optimized_sql)
        print("DB Result:", result)

        # Step 6: Analyze
        analysis = analyze_data(result)
        print("Analysis:", analysis)

        return {
            "user_query": user_query,
            "sql": optimized_sql,
            "result": result,
            "analysis": analysis
        }

    except Exception as e:
        print("🔥 FULL ERROR:", str(e))   # VERY IMPORTANT
        return {"error": str(e)}