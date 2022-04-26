import unittest
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository
from entities.shift import Shift
from entities.user import User


class TestShiftRepository(unittest.TestCase):
    def setUp(self):
        self.shift = Shift(date="12.4.2021",
                           time="6:30-12:00",
                           location="Exactum",
                           employee="Samuli")
        self.user = User(username="Samuli",
                         password="Gorilla12!",
                         role="employee")
        ShiftAppService().create_user("Samuli", "Gorilla12!", "employee")
        ShiftAppService().create_shift("12.4.2021", "6:30-12:00", "Exactum", "Samuli")

    def test_create_shift_creates_a_shift(self):
        shift = ShiftRepository().find_shift(self.shift)
        self.assertEqual(shift.date, self.shift.date)

    def test_find_user_shifts(self):
        shifts = ShiftRepository().find_user_shifts(self.user)
        print(shifts)
