import os
import unittest

from utils import TimeFormat, TimeUnit

from calendar_grid import CalendarGrid

TEST_CG = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-05-20"),
    row_unit=TimeUnit.DAY,
    n_rows=7,
    cell_unit=TimeUnit.HOUR * 2,
)


class TestCase(unittest.TestCase):
    def test_calendar_grid(self):
        self.assertEqual(TEST_CG.n_cells, 7 * 12)

    def test_write(self):
        TEST_CG.write()
        self.assertTrue(os.path.exists(TEST_CG.svg_file_path))
