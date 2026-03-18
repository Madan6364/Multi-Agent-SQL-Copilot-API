def validate_sql(query):
    # Basic SQL validation
    
    dangerous_keywords = ["DROP", "DELETE", "TRUNCATE", "ALTER"]
    
    for word in dangerous_keywords:
        if word in query.upper():
            return f"❌ Dangerous query detected: {word}"
    
    return "✅ Query is safe"