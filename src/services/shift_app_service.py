from repositories.user_repository import UserRepository
from repositories.shift_repository import ShiftRepository
from entities.user import User
from entities.shift import Shift


class ShiftAppService:

    def __init__(self):
        self._user = None
        self._user_repository = UserRepository()
        self._shift_repository = ShiftRepository()

    def create_user(self, username, password, role):
        new_user = User(username, password, role)
        self._user_repository.create_user(new_user)
    
    def create_shift(self, date, time, location, employee):
        new_shift = Shift(date, time, location, employee)
        self._shift_repository.create_shift(new_shift)
    
    def login(self,username, password):
        self._user = UserRepository().login(username, password)
        print(self._user)

    def get_current_user(self):
        return self._user


