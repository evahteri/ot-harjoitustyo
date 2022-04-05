from repositories import shift_database
from repositories.user_database import User_database
from entities.user import User

class ShiftAppService:

    def __init__(self, shift_database=shift_database, user_database = User_database):
        self._user=None
        self._shift_database = shift_database
        self._user_database = user_database
    
    def create_user(self, username, password, role):

        new_user = User(username, password, role)
        
        self._user_database.create_user(new_user)
    
        


