def generate_sql(user_query: str):

    # simple working logic (you can upgrade later using LLM)
    if "revenue" in user_query.lower():
        return "SELECT * FROM sales"

    if "india" in user_query.lower():
        return "SELECT * FROM sales WHERE region = 'India'"

    return "SELECT * FROM sales LIMIT 10"