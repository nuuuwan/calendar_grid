import os
import unittest

from utils import TimeFormat, TimeUnit

from calendar_grid import CalendarGrid

TEST_CG_WEEK = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-05-19"),
    row_unit=TimeUnit.DAY,
    n_rows=7,
    cell_unit=TimeUnit.HOUR * 2,
)

TEST_CG_MONTH = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-05-01"),
    row_unit=TimeUnit.WEEK,
    n_rows=5,
    cell_unit=TimeUnit.DAY,
)


class TestCase(unittest.TestCase):
    def test_calendar_grid(self):
        self.assertEqual(TEST_CG_WEEK.n_cells, 7 * 12)

    def test_write(self):
        for test_cg in [TEST_CG_WEEK, TEST_CG_MONTH]:
            test_cg.write()
            self.assertTrue(os.path.exists(test_cg.svg_file_path))
