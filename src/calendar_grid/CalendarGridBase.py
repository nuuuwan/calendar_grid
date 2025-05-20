import math
from dataclasses import dataclass

from utils import Log, Time, TimeDelta, TimeUnit, TimeZoneOffset, TimeFormat

log = Log("CalendarGrid")


@dataclass
class CalendarGridBase:
    time_start: Time
    row_unit: TimeUnit
    n_rows: Time
    cell_unit: TimeUnit

    @property
    def time_start_table(self) -> Time:
        return Time(
            math.floor(
                (self.time_start.ut - TimeZoneOffset.LK) / self.row_unit.seconds
            )
            * self.row_unit.seconds
            + TimeZoneOffset.LK,
        )

    @property
    def time_end(self) -> Time:
        return Time(
            self.time_start.ut + (self.n_rows - 1) * self.row_unit.seconds
        )

    @property
    def time_end_table(self) -> Time:
        return Time(
            self.time_start_table.ut + self.n_rows * self.row_unit.seconds
        )

    @property
    def time_delta_table(self) -> TimeDelta:
        return self.time_end_table - self.time_start_table

    @property
    def n_cells(self) -> int:
        return int(self.time_delta_table.dut // self.cell_unit.seconds)

    @property
    def n_cols(self) -> int:
        return int(self.n_cells // self.n_rows)

    @property
    def time_format_title(self) -> TimeFormat:
        return TimeFormat("%Y-%m-%d")

    @property
    def time_format_row_header(self) -> TimeFormat:
        if self.row_unit == TimeUnit.DAY:
            return TimeFormat("%a-%d")
        return TimeFormat.TIME_ID

    @property
    def time_format_col_header(self) -> TimeFormat:
        if self.cell_unit == TimeUnit.HOUR:
            return TimeFormat("%H")
        return TimeFormat.TIME_ID
