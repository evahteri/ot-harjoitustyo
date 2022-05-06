from db_connection import get_db_connection
from shift_db_connection import get_shift_db_connection


class CreateDatabases:
    """Class that creates databases

    """

    def __init__(self):
        """Constructor that establishes connections to both databases

        """

        self._connection = get_db_connection()
        self.shift_connection = get_shift_db_connection()

    def create_user_database(self):
        """Creates a database and a table for user information

        """

        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE user_database \
            (username TEXT NOT NULL, \
            password TEXT NOT NULL, \
            role TEXT NOT NULL)")
        self._connection.commit()
        cursor.close()

    def create_shift_database(self):
        """Creates a database and a table for shift information

        """

        cursor = self.shift_connection.cursor()
        cursor.execute("CREATE TABLE shift_database \
            (shift_id INTEGER PRIMARY KEY, \
            date TEXT, \
            time TEXT, \
            location TEXT, \
            employee TEXT)")
        self.shift_connection.commit()
        cursor.close()

    def initialize_database(self):
        """Runs both functions to establish databases

        """

        self.create_user_database()
        self.create_shift_database()


if __name__ == "__main__":
    CreateDatabases().initialize_database()
