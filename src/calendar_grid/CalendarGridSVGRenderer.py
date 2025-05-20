import os

from utils import Log, TimeFormat, _, Time

log = Log("CalendarGridSVGRenderer")


class CalendarGridSVGRenderer:
    PADDING = 10

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
    def cell_width(self):
        return 100 / (self.n_cols + 2)

    @property
    def cell_height(self):
        return 100 / (self.n_rows + 2)

    def render_cell(self, i_col, i_row, cell_width, cell_height):

        x = (i_col + 1) * self.cell_width
        y = (i_row + 1) * self.cell_height
        time_cell = Time(
            self.time_start_table.ut
            + i_row * self.row_unit.seconds
            + i_col * self.cell_unit.seconds
        )

        if time_cell.ut < self.time_start.ut or time_cell.ut > self.time_end.ut:
            return None

        FONT_SIZE_FACTOR = 10

        return _(
            "g",
            [
                _(
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
                ),
                _(
                    "text",
                    self.time_format_cell.format(time_cell),
                    dict(
                        x=x + cell_width / FONT_SIZE_FACTOR,
                        y=y + cell_height / FONT_SIZE_FACTOR,
                        font_size=cell_width / FONT_SIZE_FACTOR,
                        text_anchor="middle",
                        dominant_baseline="middle",
                        fill="#000",
                    ),
                ),
            ],
        )

    def render_header_cell(self, x, y, text):
        return _(
            "text",
            text,
            dict(
                x=x,
                y=y,
                font_size=2,
                text_anchor="middle",
                dominant_baseline="middle",
                fill="#000",
            ),
        )

    @property
    def svg_row_headers(self):
        inner = []
        for offset_x in [0, self.n_cols + 1]:
            for i_row in range(self.n_rows):
                inner.append(
                    self.render_header_cell(
                        (offset_x + 0.5) * self.cell_width,
                        (i_row + 1 + 0.5) * self.cell_height,
                        self.time_format_row_header.format(
                            Time(
                                self.time_start_table.ut
                                + i_row * self.row_unit.seconds
                            )
                        ),
                    )
                )

        return _(
            "g",
            inner,
        )

    @property
    def svg_col_headers(self):
        inner = []
        for offset_y in [0, self.n_rows + 1]:
            for i_col in range(self.n_cols):
                inner.append(
                    self.render_header_cell(
                        (i_col + 1 + 0.5) * self.cell_width,
                        (offset_y + +0.5) * self.cell_height,
                        self.time_format_col_header.format(
                            Time(
                                self.time_start_table.ut
                                + i_col * self.cell_unit.seconds
                            )
                        ),
                    )
                )

        return _(
            "g",
            inner,
        )

    @property
    def svg_inner_table(self):
        inner = []
        for i_row in range(self.n_rows):
            for i_col in range(self.n_cols):

                inner.append(
                    self.render_cell(
                        i_col,
                        i_row,
                        self.cell_width,
                        self.cell_height,
                    )
                )

        return _(
            "svg",
            inner + [self.svg_row_headers, self.svg_col_headers],
            dict(
                x=self.PADDING,
                y=self.PADDING,
                width=100 - self.PADDING * 2,
                height=100 - self.PADDING * 2,
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
        s_start = self.time_format_title.format(self.time_start)
        s_end = self.time_format_title.format(self.time_end)
        if s_start == s_end:
            return s_start

        return " to ".join(
            [
                s_start,
                s_end,
            ]
        )

    @property
    def svg_title(self):
        return _(
            "text",
            self.title,
            dict(
                x=50,
                y=self.PADDING,
                font_size=100 / max(20, len(self.title)),
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
                self.svg_rect_border,
                self.svg_inner_table,
                self.svg_title,
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
