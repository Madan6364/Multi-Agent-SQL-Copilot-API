def validate_sql(sql: str):

    if "DROP" in sql.upper():
        return False

    if "DELETE" in sql.upper():
        return False

    return True