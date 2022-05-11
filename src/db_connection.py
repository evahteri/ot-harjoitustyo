import sqlite3
from config import USERS_FILE_PATH

connection = sqlite3.connect(USERS_FILE_PATH)

connection.row_factory = sqlite3.Row


def get_db_connection():
    return connection
