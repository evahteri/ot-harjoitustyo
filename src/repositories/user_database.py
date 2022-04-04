
import sqlite3

from entities.user import User

from db_connection import get_db_connection

class User_database:

    def __init__(self, connection):
        self._connection = connection

    def create_database(self):

        cursor = self._connection.cursor()

        cursor.execute("CREATE TABLE user_database (username BLOB NOT NULL, password BLOB NOT NULL, role BLOB NOT NULL)")

        self._connection.commit()

        cursor.close()

    def create_user(self, user = User):

        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO user_database VALUES (?,?,?)", user.username, user.password, user.role)

        self._connection.commit()

        cursor.close()


user_database = User_database(get_db_connection())

