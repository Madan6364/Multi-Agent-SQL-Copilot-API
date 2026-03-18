def optimize_sql(sql):
    
    sql = sql.strip().rstrip(";")

    # ✅ If LIMIT already exists → DO NOTHING
    if "limit" in sql.lower():
        return sql + ";"

    # ✅ Otherwise add LIMIT safely
    return sql + " LIMIT 10;"