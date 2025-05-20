import math
from dataclasses import dataclass

from utils import Log, Time, TimeDelta, TimeFormat, TimeUnit, TimeZoneOffset

log = Log("CalendarGrid")


@dataclass
class CalendarGridBase:
    time_start: Time
    time_end: Time
    row_unit: TimeUnit
    cell_unit: TimeUnit

    @property
    def offset(self):
        if self.row_unit.seconds <= TimeUnit.DAY.seconds:
            return TimeZoneOffset.LK
        if self.row_unit.seconds > TimeUnit.WEEK.seconds:
            return (
                math.floor(self.time_start.ut / TimeUnit.WEEK.seconds)
                * TimeUnit.WEEK.seconds
            )

        return TimeZoneOffset.LK + TimeUnit.SECONDS_IN.DAY * 4

    @property
    def time_start_table(self) -> Time:
        return Time(
            math.floor(
                (self.time_start.ut - self.offset) / self.row_unit.seconds
            )
            * self.row_unit.seconds
            + self.offset,
        )

    @property
    def time_end_table(self) -> Time:
        return Time(
            math.ceil((self.time_end.ut - self.offset) / self.row_unit.seconds)
            * self.row_unit.seconds
            + self.offset,
        )

    @property
    def time_delta_table(self) -> TimeDelta:
        return self.time_end_table - self.time_start_table

    @property
    def n_rows(self) -> int:
        return int(self.time_delta_table.dut // self.row_unit.seconds)

    @property
    def n_cells(self) -> int:
        return int(self.time_delta_table.dut // self.cell_unit.seconds)

    @property
    def n_cols(self) -> int:
        return int(self.n_cells // self.n_rows)

    @property
    def time_format_title(self) -> TimeFormat:
        if self.time_delta_table.dut < TimeUnit.SECONDS_IN.DAY:
            return TimeFormat("%Y-%m-%d")
        if self.time_delta_table.dut < TimeUnit.SECONDS_IN.WEEK * 52:
            return TimeFormat("%Y %b")
        return TimeFormat("%Y")

    @property
    def time_format_row_header(self) -> TimeFormat:
        if self.cell_unit.seconds < TimeUnit.DAY.seconds:
            return TimeFormat("%a %d")
        if self.row_unit == TimeUnit.WEEK:
            return TimeFormat("week %W")
        return ""

    @property
    def time_format_col_header(self) -> TimeFormat:
        if self.cell_unit.seconds < TimeUnit.DAY.seconds:
            return TimeFormat("%I%p")
        if self.cell_unit.seconds == TimeUnit.DAY.seconds:
            return TimeFormat("%a")
        return TimeFormat("")

    @property
    def time_format_cell(self) -> TimeFormat:
        if self.cell_unit.seconds < TimeUnit.DAY.seconds:
            return TimeFormat("")
        if self.cell_unit == TimeUnit.DAY:
            return TimeFormat("%d")
        return TimeFormat("%b %d (Week %W)")

    @property
    def show_holiday_in_cell(self) -> bool:
        return self.cell_unit.seconds == TimeUnit.SECONDS_IN.DAY
