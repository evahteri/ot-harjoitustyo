from entities.user import User
from db_connection import get_db_connection


def return_user(row):
    return User(row["username"], row["password"], row["role"])


class UserRepository:
    """Class for handling user information

    """

    def __init__(self):
        """Establishes connection to the database

        """

        self._connection = get_db_connection()

    def create_user(self, user):
        """Creates a user

        Args:
            user (User): User type object which is saved to a table
        """

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO user_database \
            (username,password,role) \
            VALUES (?,?,?)",
                       (user.username, user.password, user.role))
        self._connection.commit()
        cursor.close()

    def find_user(self, username):
        """Finds user with the username

        Args:
            username (string): username that is searched

        Returns:
            user (User): User type object
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM user_database WHERE username=?", [username])
        row = cursor.fetchone()
        if row:
            return return_user(row)
        return False

    def login(self, username, password):
        """Login user

        Args:
            username (string): user input for username
            password (string): user input for password
        Returns:
            user (User): User type object
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM user_database WHERE (username, password)=(?,?)", (username, password))
        row = cursor.fetchone()
        if row is None:
            return None
        return return_user(row)
