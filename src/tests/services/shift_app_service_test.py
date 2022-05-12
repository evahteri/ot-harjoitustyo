from cgi import test
import unittest
import pytest
from entities.shift import Shift
from repositories.shift_repository import ShiftRepository
from repositories.user_repository import UserRepository
from services.shift_app_service import FailedLoginError, InvalidPassword, InvalidShiftInformation, NoRoleError, ShiftAppService, UsernameExistsError, UsernameTooShortError
from entities.user import User


class TestShiftAppService(unittest.TestCase):
    def setUp(self):
        self.shift_app_service = ShiftAppService()
        UserRepository().delete_data()
        self.user = User(username="Samuli",
                         password="Gorilla12!",
                         role="employee")
        self.shift_app_service.create_user("Samuli", "Gorilla12!", "employee")

    def test_login_with_valid_credentials(self):
        user = self.shift_app_service.login(
            self.user.username, self.user.password)
        self.assertEqual(user.username, self.user.username)

    def test_login_with_invalid_credentials(self):
        with pytest.raises(FailedLoginError):
            self.shift_app_service.login("Emma", "Password1!")

    def test_choose_shift(self):
        repository = ShiftRepository()
        repository.create_shift(
            Shift(date="12.1.2022", time="12:00-20:00", location="Unicafe", employee=None))
        self.shift_app_service.login(self.user.username, self.user.password)
        self.shift_app_service.choose_shift(1)
        test_shift = repository.find_user_shifts(self.user)
        self.assertEqual("Samuli", test_shift[0][4])

    def test_get_current_user(self):
        self.shift_app_service.login(self.user.username, self.user.password)
        user = self.shift_app_service.get_current_user
        self.assertEqual(user.username, self.user.username)

    def test_logout(self):
        self.shift_app_service.logout()
        self.assertEqual(None, self.shift_app_service.get_current_user)

    def test_create_shift_invalid_information(self):
        with pytest.raises(InvalidShiftInformation):
            self.shift_app_service.create_shift(
                date="", time="5:00-12:00", location="Kumpula", employee=None)

    def test_create_user_with_too_short_username(self):
        with pytest.raises(UsernameTooShortError):
            self.shift_app_service.create_user(
                username="a", password="Password1!", role="Employee")

    def test_create_user_with_no_role(self):
        with pytest.raises(NoRoleError):
            self.shift_app_service.create_user(
                username="Simo", password="Password1!", role="")

    def test_create_user_with_taken_username(self):
        with pytest.raises(UsernameExistsError):
            self.shift_app_service.create_user(
                username="Samuli", password="Password1!", role="Employee")

    def test_create_user_with_invalid_password_no_special_characters(self):
        with pytest.raises(InvalidPassword):
            self.shift_app_service.create_user(
                username="Simo", password="Password1", role="Employee")

    def test_create_user_with_invalid_password_no_numbers(self):
        with pytest.raises(InvalidPassword):
            self.shift_app_service.create_user(
                username="Simo", password="Password!", role="Employee")

    def test_create_user_with_invalid_password_too_short(self):
        with pytest.raises(InvalidPassword):
            self.shift_app_service.create_user(
                username="Simo", password="Pas1!", role="Employee")

    def test_create_user_with_invalid_password_no_uppers(self):
        with pytest.raises(InvalidPassword):
            self.shift_app_service.create_user(
                username="Simo", password="password1!", role="Employee")

    def test_create_user_with_invalid_password_no_lowers(self):
        with pytest.raises(InvalidPassword):
            self.shift_app_service.create_user(
                username="Simo", password="PASSWORD1!", role="Employee")
