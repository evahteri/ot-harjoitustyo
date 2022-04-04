import sqlite3

connection = sqlite3.connect("users.db")

connection.row_factory = sqlite3.Row

def get_db_connection():
    return connection