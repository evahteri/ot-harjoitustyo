from db_connection import get_db_connection

class CreateDatabases:

    def __init__(self):
        self._connection = get_db_connection()

    def create_user_database(self):
        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE user_database \
            (username TEXT NOT NULL, \
            password TEXT NOT NULL, \
            role TEXT NOT NULL)")
        self._connection.commit()
        cursor.close()

if __name__ == "__main__":
    c = CreateDatabases()
    c.create_user_database()
