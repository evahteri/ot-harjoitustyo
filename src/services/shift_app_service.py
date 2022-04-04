from repositories import (shift_database as default_shift_database)
from repositories import (user_database as default_user_database)
from entities import user

class ShiftAppService:

    def __init__(self, shift_database=default_shift_database, user_database = default_user_database):
        self._user=None
        self._shift_database = shift_database
        self._user_database = user_database
    
    def create_user(self, username, password, role):

        self_user = user.User(username, password, role)
