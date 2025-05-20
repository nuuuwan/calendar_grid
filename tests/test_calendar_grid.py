import os
import unittest

from utils import TimeFormat, TimeUnit

from calendar_grid import CalendarGrid

TEST_CG = CalendarGrid(
    time_start=TimeFormat.DATE.parse("2025-05-20"),
    time_end=TimeFormat.DATE.parse("2025-05-27"),
    cell_unit=TimeUnit.HOUR * 2,
    row_unit=TimeUnit.DAY,
)


class TestCase(unittest.TestCase):
    def test_calendar_grid(self):
        self.assertEqual(TEST_CG.n_cells, 7 * 12)
        self.assertEqual(TEST_CG.n_rows, 7)

    def test_write(self):
        TEST_CG.write()
        self.assertTrue(os.path.exists(TEST_CG.svg_file_path))
        os.startfile(TEST_CG.svg_file_path)
