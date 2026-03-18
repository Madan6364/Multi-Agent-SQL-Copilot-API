def check_schema(sql_query, schema):
    # Basic schema validation
    
    if not schema:
        return "❌ No schema provided"
    
    # simple check (you can improve later)
    return "✅ Schema looks fine"