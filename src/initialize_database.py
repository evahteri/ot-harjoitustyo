from db_connection import get_db_connection
from shift_db_connection import get_shift_db_connection

class CreateDatabases:

    def __init__(self):
        self._connection = get_db_connection()
        self.shift_connection = get_shift_db_connection()

    def create_user_database(self):
        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE user_database \
            (username TEXT NOT NULL, \
            password TEXT NOT NULL, \
            role TEXT NOT NULL)")
        self._connection.commit()
        cursor.close()
    
    def create_shift_database(self):
        cursor = self.shift_connection.cursor()
        cursor.execute("CREATE TABLE shift_database \
            (date TEXT NOT NULL, \
            time TEXT NOT NULL, \
            location TEXT NOT NULL, \
            employee TEXT)")
        self.shift_connection.commit()
        cursor.close()

    def initialize_database(self):
        self.create_user_database()
        self.create_shift_database()


if __name__ == "__main__":
    CreateDatabases().initialize_database()
