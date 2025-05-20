import os

from utils import Log, TimeFormat, _

log = Log("CalendarGridSVGRenderer")


class CalendarGridSVGRenderer:
    @property
    def svg_file_path(self):
        return os.path.join(
            "images",
            ".".join(
                [
                    "calendar-grid",
                    TimeFormat.TIME_ID.format(self.time_start),
                    TimeFormat.TIME_ID.format(self.time_end),
                    f"{self.cell_unit.seconds}s",
                    f"{self.row_unit.seconds}s",
                    "svg",
                ]
            ),
        )

    @property
    def svg_inner_table(self):
        g = []
        cell_width = 100 / self.n_cols
        cell_height = 100 / self.n_rows
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):
                x = i_col * cell_width
                y = i_row * cell_height
                g.append(
                    _(
                        "rect",
                        None,
                        dict(
                            x=x,
                            y=y,
                            width=cell_width,
                            height=cell_height,
                            fill="#fff",
                            stroke="#000",
                            stroke_width=0.5,
                        ),
                    )
                )
        PADDING = 10
        return _(
            "svg",
            g,
            dict(
                x=PADDING,
                y=PADDING,
                width=100 - PADDING * 2,
                height=100 - PADDING * 2,
                viewBox="0 0 100 100",
            ),
        )

    @property
    def svg_rect_border(self):
        return _(
            "rect",
            None,
            dict(
                x=0,
                y=0,
                width="100",
                height="100",
                fill="#f004",
            ),
        )

    @property
    def svg(self):
        return _(
            "svg",
            [
                self.svg_inner_table,
                self.svg_rect_border,
            ],
            dict(
                width=3400 * 0.5,
                height=2400 * 0.5,
                viewBox="0 0 100 100",
                preserveAspectRatio="none",
            ),
        )

    def write(self):
        self.svg.store(self.svg_file_path)
        log.info(f"Wrote {self.svg_file_path}")
