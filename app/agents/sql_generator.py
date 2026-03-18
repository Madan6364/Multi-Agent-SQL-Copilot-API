def generate_sql(user_query):
    
    user_query = user_query.lower()

    # ✅ FIXED SQL
    if "show all users" in user_query:
        return "SELECT * FROM sales LIMIT 10;"
    
    if "total revenue" in user_query:
        return "SELECT SUM(revenue) FROM sales;"
    
    if "region" in user_query:
        return "SELECT region, SUM(revenue) FROM sales GROUP BY region;"
    
    # default fallback
    return "SELECT * FROM sales LIMIT 10;"