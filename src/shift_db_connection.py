import sqlite3
from config import SHIFTS_FILE_PATH

connection = sqlite3.connect(SHIFTS_FILE_PATH)

connection.row_factory = sqlite3.Row


def get_shift_db_connection():
    return connection
