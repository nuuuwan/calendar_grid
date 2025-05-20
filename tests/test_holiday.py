import unittest
from calendar_grid import Holidays
from utils import TimeFormat


class TestCase(unittest.TestCase):
    def test_list(self):
        holidays = Holidays.list()
        self.assertEqual(len(holidays), 27)

    def test_get_holiday(self):
        self.assertIsNotNone(
            Holidays.get_holiday(TimeFormat.DATE.parse("2025-05-01"))
        )
        self.assertIsNone(
            Holidays.get_holiday(TimeFormat.DATE.parse("2025-05-02"))
        )
