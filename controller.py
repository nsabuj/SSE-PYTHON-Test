from db import get_db


def insert_todo(task, status):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO todos(task, status) VALUES (?, ?)"
    cursor.execute(statement, [task, status])
    db.commit()
    return True


def update_todo(id, status):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE todos SET status = ? WHERE id = ?"
    cursor.execute(statement, [status , id])
    db.commit()
    return True


def delete_todo(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM todos WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def filter_todo(status):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, task, status FROM todos WHERE status = ?"
    cursor.execute(statement, [status])
    return cursor.fetchall()

def search_todo(string):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, task, status FROM todos WHERE task LIKE ? "
    cursor.execute(statement, ['%'+string+'%'])
    return cursor.fetchall()

def get_todos():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, task, status FROM todos"
    cursor.execute(query)
    return cursor.fetchall()