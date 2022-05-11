from repositories.user_repository import UserRepository
from repositories.shift_repository import ShiftRepository
from entities.user import User
from entities.shift import Shift


class FailedLoginError(Exception):
    pass


class InvalidPassword(Exception):
    pass


class InvalidShiftInformation(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class UsernameTooShortError(Exception):
    pass


class NoRoleError(Exception):
    pass


class ShiftAppService:
    """Class that takes care of the application logic

    """

    def __init__(self):
        """Constructor that stores current user and establishes repositories

        """

        self._user = None
        self._user_repository = UserRepository()
        self._shift_repository = ShiftRepository()

    @property
    def get_current_user(self):
        """Calling this will return the user that is logged in

        Returns:
            User: current user
        """
        current_user = self._user
        return current_user

    def set_current_user(self, user):
        """Sets the current user to the user from the arg

        Args:
            user (User): User object that will be assigned to self._user
        """
        self._user = user

    def _check_password_validity(self, password):
        special_characters = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
                              ":", ";", "<", "=", ">", "?", "@", "[", "]",
                              "^", "_", "`", "{", "|", "}", "~", "."]
        valid = True
        if len(password) < 8:
            valid = False
        if not any(i.isupper() for i in password):
            valid = False
        if not any(i.isdigit() for i in password):
            valid = False
        if not any(i.islower() for i in password):
            valid = False
        if not any(i in special_characters for i in password):
            valid = False
        return valid

    def create_user(self, username, password, role):
        """Creates a user

        Args:
            username (string): username which user has chosen to use
            password (string): password that user has chosen to use
            role (string): choice between employer and employee

        Raises:
            InvalidPassword: if password doesn't meet the requirements
        """
        if len(username) < 3:
            raise UsernameTooShortError("Username is too short")
        if role == "":
            raise NoRoleError("No role chosen")
        if self._check_password_validity(password) is False:
            raise InvalidPassword("Invalid password")
        if self._user_repository.find_user(username=username):
            raise UsernameExistsError(f"User {username} already exists!")

        new_user = User(username, password, role)
        self._user_repository.create_user(new_user)

    def create_shift(self, date, time, location, employee):
        """Creates a new shift

        Args:
            date (string): date for the shift (ie. 30.4.2022)
            time (string): time of day (ie. 6:30 - 12:00)
            location (string): place that shift takes place
            employee (string/None): employee for the shift (if this is a avalailable shift,
            employee arg can be Nonetype)
        """
        if len(date) == 0 or len(time) == 0 or len(location) == 0:
            raise InvalidShiftInformation("Invalid shift information")

        new_shift = Shift(date, time, location, employee)
        self._shift_repository.create_shift(new_shift)

    def login(self, username, password):
        """Logs user in

        Args:
            username (string): username
            password (string): password

        Raises:
            FailedLoginError: if username and password combination cannot be found in table

        Returns:
            User: returns a user if login is successful
        """

        user = UserRepository().login(username, password)
        if not user:
            raise FailedLoginError("Invalid username or password")
        self.set_current_user(user)
        return self._user

    def logout(self):
        """Logs user out, a.k.a. sets current user to None
        """
        self.set_current_user(None)

    def choose_shift(self, shift_id):
        """Chooses the shift via shift repository

        Args:
            shift_id (int): id number that matches the selected shift
        """
        self._shift_repository.choose_shift(shift_id, self._user)
