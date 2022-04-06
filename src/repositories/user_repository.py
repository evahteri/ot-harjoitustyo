import sqlite3

from entities.user import User

from db_connection import get_db_connection

class UserRepository:

    def __init__(self):
        self._connection = get_db_connection()

    def create_database(self):
        cursor = self._connection.cursor()
        cursor.execute("CREATE TABLE user_database (username TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL)")
        self._connection.commit()
        cursor.close()

    def create_user(self, user):
        cursor = self._connection.cursor()
        print(user.username)
        print("tuo oli käyttäjä")
        cursor.execute("INSERT INTO user_database(username,password,role) VALUES (?,?,?)", (user.username, user.password, user.role))
        self._connection.commit()
        cursor.close()


