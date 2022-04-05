
from repositories.user_repository import UserRepository
from entities.user import User

class ShiftAppService:

    def __init__(self, user_repository = UserRepository):
        self._user=None
        self._user_repository = user_repository
    
    def create_user(self, username, password, role):
        new_user = User(username, password, role)
        self._user_repository.create_user(new_user)
    
        


