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

    @staticmethod
    def render_table_cell(x, y, cell_width, cell_height):
        return _(
            "rect",
            None,
            dict(
                x=x,
                y=y,
                width=cell_width,
                height=cell_height,
                fill="none",
                stroke="#000",
                stroke_width=0.1,
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
                    self.render_table_cell(
                        x,
                        y,
                        cell_width,
                        cell_height,
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
                width=100,
                height=100,
                fill="#8881",
            ),
        )

    @property
    def title(self):
        return " to ".join(
            [
                TimeFormat.TIME.format(self.time_start),
                TimeFormat.TIME.format(self.time_end),
            ]
        )

    @property
    def svg_title(self):
        return _(
            "text",
            self.title,
            dict(
                x=50,
                y=5,
                font_size=100 / len(self.title),
                text_anchor="middle",
                dominant_baseline="middle",
                fill="#000",
            ),
        )

    @property
    def svg(self):
        return _(
            "svg",
            [
                self.svg_inner_table,
                self.svg_title,
                self.svg_rect_border,
            ],
            dict(
                width=1440,
                height=1080,
                viewBox="0 0 100 100",
                preserveAspectRatio="none",
                font_family="Consolas",
            ),
        )

    def write(self):
        self.svg.store(self.svg_file_path)
        log.info(f"Wrote {self.svg_file_path}")
