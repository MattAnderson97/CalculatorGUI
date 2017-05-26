from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

from src.gui.NumBtn import NumBtn
from src.gui.OpBtn import OpBtn


class CalcButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(250)

        self.btn_0 = NumBtn("0")
        self.btn_1 = NumBtn("1")
        self.btn_2 = NumBtn("2")
        self.btn_3 = NumBtn("3")
        self.btn_4 = NumBtn("4")
        self.btn_5 = NumBtn("5")
        self.btn_6 = NumBtn("6")
        self.btn_7 = NumBtn("7")
        self.btn_8 = NumBtn("8")
        self.btn_9 = NumBtn("9")
        self.btn_point = NumBtn(".")
        self.btn_equals = NumBtn("=")
        self.btn_add = OpBtn("+")
        self.btn_sub = OpBtn("−")
        self.btn_mult = OpBtn("×")
        self.btn_div = OpBtn("÷")

        bottom_row_layout = QHBoxLayout()
        mid_lower_row_layout = QHBoxLayout()
        mid_upper_row_layout = QHBoxLayout()
        top_row_layout = QHBoxLayout()

        bottom_row_layout.addWidget(self.btn_point)
        bottom_row_layout.addWidget(self.btn_0)
        bottom_row_layout.addWidget(self.btn_equals)

        mid_lower_row_layout.addWidget(self.btn_1)
        mid_lower_row_layout.addWidget(self.btn_2)
        mid_lower_row_layout.addWidget(self.btn_3)

        mid_upper_row_layout.addWidget(self.btn_4)
        mid_upper_row_layout.addWidget(self.btn_5)
        mid_upper_row_layout.addWidget(self.btn_6)

        top_row_layout.addWidget(self.btn_7)
        top_row_layout.addWidget(self.btn_8)
        top_row_layout.addWidget(self.btn_9)

        bottom_row = QWidget()
        bottom_row.setLayout(bottom_row_layout)
        mid_lower_row = QWidget()
        mid_lower_row.setLayout(mid_lower_row_layout)
        mid_upper_row = QWidget()
        mid_upper_row.setLayout(mid_upper_row_layout)
        top_row = QWidget()
        top_row.setLayout(top_row_layout)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(top_row)
        btn_layout.addWidget(mid_upper_row)
        btn_layout.addWidget(mid_lower_row)
        btn_layout.addWidget(bottom_row)

        side_btns_layout = QVBoxLayout()
        side_btns_layout.addWidget(self.btn_add)
        side_btns_layout.addWidget(self.btn_sub)
        side_btns_layout.addWidget(self.btn_mult)
        side_btns_layout.addWidget(self.btn_div)

        side_btns = QWidget()
        side_btns.setFixedWidth(60)
        side_btns.setLayout(side_btns_layout)

        side_btns.setAutoFillBackground(True)
        side_btns_palette = side_btns.palette()
        side_btns_palette.setColor(side_btns.backgroundRole(), QColor(50, 50, 50))
        side_btns.setPalette(side_btns_palette)

        main_btns = QWidget()
        main_btns.setLayout(btn_layout)

        calc_buttons_layout = QHBoxLayout()
        calc_buttons_layout.addWidget(main_btns)
        calc_buttons_layout.addWidget(side_btns)

        calc_buttons_layout.setContentsMargins(0, 0, 0, 0)
        calc_buttons_layout.setSpacing(0)

        self.setLayout(calc_buttons_layout)