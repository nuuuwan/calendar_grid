import os
import unittest
import shutil
from utils import TimeFormat, TimeUnit

from calendar_grid import CalendarGrid

TEST_CG_WEEK = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-05-12"),
    time_end=TimeFormat.DATE.parse("2025-05-18"),
    row_unit=TimeUnit.DAY,
    cell_unit=TimeUnit.HOUR * 2,
)

TEST_CG_MONTH = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-05-01"),
    time_end=TimeFormat.DATE.parse("2025-05-31"),
    row_unit=TimeUnit.WEEK,
    cell_unit=TimeUnit.DAY,
)
TEST_CG_QUARTER_BY_WEEK = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-04-01"),
    time_end=TimeFormat.DATE.parse("2025-06-30"),
    row_unit=TimeUnit(TimeUnit.WEEK.seconds * 4),
    cell_unit=TimeUnit.WEEK,
)

TEST_CG_YEAR_BY_WEEK = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-01-01"),
    time_end=TimeFormat.DATE.parse("2025-12-31"),
    row_unit=TimeUnit(TimeUnit.WEEK.seconds * 13),
    cell_unit=TimeUnit.WEEK,
)
TEST_CG_YEAR_BY_WEEK4 = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-01-01"),
    time_end=TimeFormat.DATE.parse("2025-12-31"),
    row_unit=TimeUnit(TimeUnit.WEEK.seconds * 12),
    cell_unit=TimeUnit(TimeUnit.WEEK.seconds * 4),
)

LIST_TEST_CG = [
    TEST_CG_WEEK,
    TEST_CG_MONTH,
    TEST_CG_QUARTER_BY_WEEK,
    TEST_CG_YEAR_BY_WEEK,
    TEST_CG_YEAR_BY_WEEK4,
]


class TestCase(unittest.TestCase):

    def before(self):
        if os.path.exists("images"):
            shutil.rmtree("images")
        os.makedirs("images", exist_ok=True)

    def test_write(self):
        self.before()
        for test_cg in LIST_TEST_CG:
            test_cg.write()
            self.assertTrue(os.path.exists(test_cg.svg_file_path))
