import unittest
from services.shift_app_service import ShiftAppService
from repositories.shift_repository import ShiftRepository
from entities.shift import Shift


class TestShiftRepository(unittest.TestCase):
    def setUp(self):
        self.shift = Shift(date="12.4.2021",
                        time="6:30-12:00", 
                        location="Exactum",
                        employee="Samuli")
        ShiftAppService().create_shift("12.4.2021", "6:30-12:00", "Exactum", "Samuli")


    def test_create_shift_creates_a_shift(self):
        shift = ShiftRepository().find_shift(self.shift)
        print(shift)
