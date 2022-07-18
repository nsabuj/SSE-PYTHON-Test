import sqlite3
DATABASE_NAME = "todo.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_table():
    table = """CREATE TABLE IF NOT EXISTS todos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
				status TEXT NOT NULL)
            """
    
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute(table)