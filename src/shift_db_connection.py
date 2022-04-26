import sqlite3

connection = sqlite3.connect("shifts.db")

connection.row_factory = sqlite3.Row


def get_shift_db_connection():
    return connection
