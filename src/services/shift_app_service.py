from repositories.user_repository import UserRepository
from repositories.shift_repository import ShiftRepository
from entities.user import User
from entities.shift import Shift


class FailedLoginError(Exception):
    pass


class InvalidPassword(Exception):
    pass


class ShiftAppService:

    def __init__(self):
        self._user = None
        self._user_repository = UserRepository()
        self._shift_repository = ShiftRepository()

    def create_user(self, username, password, role):
        if self._password_checker(password) is False:
            raise InvalidPassword("Invalid password")
        new_user = User(username, password, role)
        self._user_repository.create_user(new_user)

    def create_shift(self, date, time, location, employee):
        new_shift = Shift(date, time, location, employee)
        self._shift_repository.create_shift(new_shift)

    def login(self, username, password):
        self._user = UserRepository().login(username, password)
        if not self._user:
            raise FailedLoginError("Invalid username or password")
        return self._user

    def get_current_user(self):
        return self._user

    def _password_checker(self, password):
        special_characters = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
                              ":", ";", "<", "=", ">", "?", "@", "[", "]",
                              "^", "_", "`", "{", "|", "}", "~", "."]
        valid = True
        if len(password) < 8:
            valid = False
        if not any(i.isupper for i in password):
            valid = False
        if not any(i.isdigit() for i in password):
            valid = False
        if not any(i.islower() for i in password):
            valid = False
        if not any(i in special_characters for i in password):
            valid = False
        return valid
