import sqlite3

class Create_databases:

    def __init__(self):

        self._connection = sqlite3.connect("users.db")

    def create_user_database(self):

        cursor = self._connection.cursor()

        cursor.execute("CREATE TABLE user_database (username TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL)")

        self._connection.commit()

        cursor.close()

    
if __name__ == "__main__":
    c = Create_databases()
    c.create_user_database()