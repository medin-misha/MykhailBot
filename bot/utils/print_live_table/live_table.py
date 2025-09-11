from PIL import ImageFilter, ImageDraw, Image, ImageFont
import numpy as np
from datetime import datetime, timedelta
import io

class LiveTableComputer:
    @staticmethod
    def calculate(user_birthday: str):
        user_birthday_object = datetime.strptime(user_birthday, "%d/%m/%Y")
        now_object = datetime.now()
        week = 7
        arr_width = 68
        arr_height = 68

        life_weeks = (now_object - user_birthday_object).days / week
        fill_lines = int(life_weeks // arr_width)
        fill_cells_in_last_line = int(life_weeks % arr_width)

        table_array = np.zeros((arr_height, arr_width), dtype=int)
        if fill_lines > 0:
            table_array[:fill_lines, :] = 1
        if fill_cells_in_last_line > 0 and fill_lines < arr_height:
            table_array[fill_lines, :fill_cells_in_last_line] = 1
        return table_array


class LiveTableDraw:
    def __init__(self, name: str, birthday_date: str):
        self.name = name
        self.birthday_date = birthday_date
        self.colors: dict = {
            "background": "#ffffff",
            "header": "#9372DA",
            "footer": "#9372DA",
            "text_color": "#ffffff",
            "fill_cell": "#9372DA",
            "cell": "#c9c9c9",
        }
        self.header_text: dict = {
            "live_table": "LIVE TABLE",
            "for": self.name,
            "by": "@medinmisha",
            "dates": f"{birthday_date} - {(datetime.strptime(birthday_date, '%d/%m/%Y') + timedelta(weeks=4640)).strftime('%d/%m/%Y')}",
        }
        self.page_size = (297 * 4, 420 * 4)
        self.top_margin = (self.page_size[1] * 0.15) + 100
        self.bottom_margin = self.page_size[1] - (self.page_size[1] * 0.1) + 100
        self.left_margin = 65.5
        self.cell_size = 12

    def draw_cell(self, idraw: ImageDraw, line: int, cell: int, is_fill: int):
        x = int(self.left_margin + (self.cell_size * 1.3 * cell))
        y = int(self.top_margin + (self.cell_size * 1.3 * line))
        x1 = int(x + self.cell_size)
        y1 = int(y + self.cell_size)
        idraw.rectangle(
            # x и y первой точки, и x и y второй точки
            (x, y, x1, y1),
            fill=self.colors["fill_cell"] if is_fill else self.colors["cell"],
        )

    def draw_header_background(self, idraw: ImageDraw):
        x = 0
        y = 0
        x1 = self.page_size[0]
        y1 = self.page_size[1] * 0.15
        idraw.rectangle(
            # x и y первой точки, и x и y второй точки
            (x, y, x1, y1),
            fill=self.colors["header"],
        )

    def draw_footer_background(self, idraw: ImageDraw):
        x = 0
        y = self.page_size[1] - self.page_size[1] * 0.1
        x1 = self.page_size[0]
        y1 = self.page_size[1]
        idraw.rectangle(
            # x и y первой точки, и x и y второй точки
            (x, y, x1, y1),
            fill=self.colors["footer"],
        )

    def draw_header_date_text(self, idraw: ImageDraw):
        x = 20
        y = 170
        font = ImageFont.truetype("static/Montserrat-Black.ttf", size=52)
        idraw.text(
            (x, y), self.header_text["dates"], self.colors["text_color"], font=font
        )

    def draw_header_table_name_text(self, idraw: ImageDraw):
        x = 20
        y = 0
        font = ImageFont.truetype("static/Montserrat-BlackItalic.ttf", size=100)
        idraw.text(
            (x, y), self.header_text["live_table"], self.colors["text_color"], font=font
        )

    def draw_header_for_user(self, idraw: ImageDraw):
        x = 20
        y = 110
        font = ImageFont.truetype("static/Montserrat-BlackItalic.ttf", size=52)
        idraw.text(
            (x, y),
            f"for {self.header_text['for']}",
            self.colors["text_color"],
            font=font,
        )

    def draw_footer_by(self, idraw: ImageDraw):
        x = 20
        y = 1575
        font = ImageFont.truetype("static/Montserrat-BlackItalic.ttf", size=32)
        idraw.text(
            (x, y),
            f"for {self.header_text['by']}",
            self.colors["text_color"],
            font=font,
        )

    def create_table(self) -> io.BytesIO:
        img = Image.new(
            mode="RGBA", size=self.page_size, color=self.colors["background"]
        )
        idraw = ImageDraw.Draw(img)
        self.draw_header_background(idraw=idraw)
        self.draw_footer_background(idraw=idraw)
        table_array = LiveTableComputer.calculate(self.birthday_date)
        for l_index, line in enumerate(table_array):
            for c_index, cell in enumerate(line):
                self.draw_cell(idraw=idraw, line=l_index, cell=c_index, is_fill=cell)
        self.draw_header_date_text(idraw=idraw)
        self.draw_header_table_name_text(idraw=idraw)
        self.draw_header_for_user(idraw=idraw)
        self.draw_footer_by(idraw=idraw)
        buffer = io.BytesIO()
        img.save(buffer, format="png")
        buffer.seek(0)
        return buffer


if __name__ == "__main__":
    table = LiveTableDraw(name="misha", birthday_date="03/09/2008")
    table.create_table()
