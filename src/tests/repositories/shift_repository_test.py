import unittest
import pytest
from repositories.user_repository import UserRepository
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import NoShiftsError, ShiftRepository
from entities.shift import Shift
from entities.user import User


class TestShiftRepository(unittest.TestCase):
    def setUp(self):
        ShiftRepository().delete_data()
        UserRepository().delete_data()
        self.shift = Shift(date="12.4.2021",
                           time="6:30-12:00",
                           location="Exactum",
                           employee="Samuli")
        self.user = User(username="Samuli",
                         password="Gorilla12!",
                         role="employee")
        ShiftAppService().create_user("Samuli", "Gorilla12!", "employee")
        ShiftAppService().create_shift("12.4.2021", "6:30-12:00", "Exactum", "Samuli")
        ShiftAppService().create_shift("12.5.2022", "7:00-12:00", "Physicum", "Samuli")
        ShiftAppService().create_shift("11.2.2022", "7:00-14:00", "Unicafe", employee=None)

    def test_create_shift_creates_a_shift(self):
        shift = ShiftRepository().find_shift(self.shift)
        self.assertEqual(shift.date, self.shift.date)

    def test_find_user_shifts(self):
        shifts = ShiftRepository().find_user_shifts(self.user)
        self.assertEqual(shifts[0][1], self.shift.date)

    def test_find_available_shifts(self):
        shifts = ShiftRepository().find_available_shifts()
        self.assertEqual(shifts[0][4], None)

    def test_find_all_shifts(self):
        shifts = [(1, "12.4.2021", "6:30-12:00", "Exactum", "Samuli"), (2, "12.5.2022",
                                                                        "7:00-12:00", "Physicum", "Samuli"), (3, "11.2.2022", "7:00-14:00", "Unicafe", None)]
        all_shifts = ShiftRepository().find_all_shifts()
        self.assertEqual(shifts, all_shifts)

    def test_choose_shift(self):
        ShiftRepository().choose_shift(3, self.user)
        user_shifts = ShiftRepository().find_user_shifts(self.user)
        shifts = [(1, "12.4.2021", "6:30-12:00", "Exactum", "Samuli"), (2, "12.5.2022",
                                                                        "7:00-12:00", "Physicum", "Samuli"), (3, "11.2.2022", "7:00-14:00", "Unicafe", "Samuli")]
        self.assertEqual(user_shifts, shifts)

    def test_find_available_shifts_has_no_shifts(self):
        ShiftRepository().delete_data()
        with pytest.raises(NoShiftsError):
            ShiftRepository().find_available_shifts()
