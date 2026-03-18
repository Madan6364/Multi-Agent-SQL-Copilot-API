import sqlite3
import os

# ✅ Ensure DB is created in correct folder
BASE_DIR = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_DIR, "sales.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ✅ Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    revenue INTEGER,
    region TEXT
)
""")

# ✅ Insert data
cursor.execute("INSERT INTO sales (product, revenue, region) VALUES ('Laptop', 1000, 'India')")
cursor.execute("INSERT INTO sales (product, revenue, region) VALUES ('Mobile', 500, 'USA')")
cursor.execute("INSERT INTO sales (product, revenue, region) VALUES ('Tablet', 300, 'UK')")

conn.commit()
conn.close()

print("✅ Database created successfully with data!")