import unittest
from services.shift_app_service import ShiftAppService
from entities.user import User


class TestShiftAppService(unittest.TestCase):
    def setUp(self):
        self.user = User(username="Samuli",
                         password="Gorilla12!",
                         role="employee")
        ShiftAppService().create_user("Samuli", "Gorilla12!", "employee")

    def test_login_with_valid_credentials(self):
        user = ShiftAppService().login(self.user.username, self.user.password)
        self.assertEqual(user.username, self.user.username)

