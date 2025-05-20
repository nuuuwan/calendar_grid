from dataclasses import dataclass

from utils import Log, Time, TimeDelta, TimeUnit

log = Log("CalendarGrid")


@dataclass
class CalendarGridBase:
    time_start: Time
    time_end: Time
    cell_unit: TimeUnit
    row_unit: TimeUnit

    @property
    def time_delta(self) -> TimeDelta:
        return self.time_end - self.time_start

    @property
    def n_cells(self) -> int:
        return int(self.time_delta.dut // self.cell_unit.seconds)

    @property
    def n_rows(self) -> int:
        return int(self.time_delta.dut // self.row_unit.seconds)

    @property
    def n_cols(self) -> int:
        return int(self.n_cells // self.n_rows)
