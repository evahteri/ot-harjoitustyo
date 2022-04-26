import unittest
from services.shift_app_service import ShiftAppService
from repositories.user_repository import UserRepository
from entities.user import User
from initialize_database import CreateDatabases


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user = User(username="Samuli",
                         password="Gorilla12!",
                         role="employee")
        ShiftAppService().create_user("Samuli", "Gorilla12!", "employee")

    def test_create_user_creates_a_user(self):
        user = UserRepository().find_user("Samuli")
        self.assertEqual(user.username, self.user.username)
