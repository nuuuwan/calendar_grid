import math
from dataclasses import dataclass

from utils import Log, Time, TimeDelta, TimeUnit, TimeZoneOffset

log = Log("CalendarGrid")


@dataclass
class CalendarGridBase:
    time_start: Time
    time_end: Time
    cell_unit: TimeUnit
    row_unit: TimeUnit

    @property
    def time_start_table(self) -> Time:
        return Time(
            math.floor(
                (self.time_start.ut - TimeZoneOffset.LK)
                / self.row_unit.seconds
            )
            * self.row_unit.seconds
            + TimeZoneOffset.LK,
        )

    @property
    def time_end_table(self) -> Time:
        return Time(
            math.ceil(
                (self.time_end.ut - TimeZoneOffset.LK) / self.row_unit.seconds
            )
            * self.row_unit.seconds
            + TimeZoneOffset.LK,
        )

    @property
    def time_delta_table(self) -> TimeDelta:
        return self.time_end_table - self.time_start_table

    @property
    def n_cells(self) -> int:
        return int(self.time_delta_table.dut // self.cell_unit.seconds)

    @property
    def n_rows(self) -> int:
        return int(self.time_delta_table.dut // self.row_unit.seconds)

    @property
    def n_cols(self) -> int:
        return int(self.n_cells // self.n_rows)
