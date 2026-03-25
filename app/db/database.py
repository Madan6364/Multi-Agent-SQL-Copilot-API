import sqlite3
import os

# Go to project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DB_PATH = os.path.join(BASE_DIR, "sales.db")

def get_connection():
    return sqlite3.connect(DB_PATH)