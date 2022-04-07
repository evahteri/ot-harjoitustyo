from entities.user import User

from db_connection import get_db_connection


def return_user(row):
    return User(row["username"], row["password"], row["role"])


class UserRepository:

    def __init__(self):
        self._connection = get_db_connection()

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO user_database \
            (username,password,role) \
            VALUES (?,?,?)",
                       (user.username, user.password, user.role))
        self._connection.commit()
        cursor.close()

    def find_user(self, username):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM user_database WHERE username=?", [username])
        row = cursor.fetchone()
        return return_user(row)
