def analyze_data(data):
    if isinstance(data, dict) and "error" in data:
        return data
    
    if not data:
        return {"summary": "No data found", "rows": 0}
    
    return {
        "summary": "Data analysis completed",
        "rows": len(data)
    }