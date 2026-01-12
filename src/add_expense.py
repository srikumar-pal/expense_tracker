import sqlite3
from src.db import connect_db

def add_expense(amount, category, date, note=""):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
        (amount, category, date, note)
    )
    conn.commit()
    conn.close()
