import re
from math import ceil

from PyQt5.QtWidgets import QVBoxLayout

from src.gui.CalcButtons import CalcButtons
from src.gui.CalcDisplay import CalcDisplay


class MainLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # self.window_bar = WindowBar()
        self.calc_display = CalcDisplay()
        self.calc_buttons = CalcButtons()
        self.lines = 1

        self.clear_display = False

        # self.addWidget(self.window_bar)
        self.addWidget(self.calc_display)
        self.addWidget(self.calc_buttons)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

        self.calc_buttons.btn_0.clicked.connect(lambda: self.update_display("0", False))
        self.calc_buttons.btn_1.clicked.connect(lambda: self.update_display("1", False))
        self.calc_buttons.btn_2.clicked.connect(lambda: self.update_display("2", False))
        self.calc_buttons.btn_3.clicked.connect(lambda: self.update_display("3", False))
        self.calc_buttons.btn_4.clicked.connect(lambda: self.update_display("4", False))
        self.calc_buttons.btn_5.clicked.connect(lambda: self.update_display("5", False))
        self.calc_buttons.btn_6.clicked.connect(lambda: self.update_display("6", False))
        self.calc_buttons.btn_7.clicked.connect(lambda: self.update_display("7", False))
        self.calc_buttons.btn_8.clicked.connect(lambda: self.update_display("8", False))
        self.calc_buttons.btn_9.clicked.connect(lambda: self.update_display("9", False))
        self.calc_buttons.btn_point.clicked.connect(lambda: self.update_display(".", False))
        self.calc_buttons.btn_add.clicked.connect(lambda: self.update_display("+", False))
        self.calc_buttons.btn_sub.clicked.connect(lambda: self.update_display("-", False))
        self.calc_buttons.btn_mult.clicked.connect(lambda: self.update_display("*", False))
        self.calc_buttons.btn_div.clicked.connect(lambda: self.update_display("/", False))
        self.calc_buttons.btn_open_bracket.clicked.connect(lambda: self.update_display("(", False))
        self.calc_buttons.btn_close_bracket.clicked.connect(lambda: self.update_display(")", False))
        self.calc_buttons.btn_pi.clicked.connect(lambda: self.update_display("π", False))
        self.calc_buttons.btn_pow.clicked.connect(lambda: self.update_display('^', False))
        self.calc_buttons.btn_more.clicked.connect(self.calc_buttons.toggle_extras)
        self.calc_display.btn_back.clicked.connect(self.del_char)

    def update_display(self, text, result):
        if not result:
            if self.clear_display:
                self.calc_display.display_txt.setText("0")
                self.clear_display = False

            if self.calc_display.display_txt.text() == "0":
                if re.match(r'^[0-9()π^]*$', text):
                    self.calc_display.display_txt.setText(text)
                else:
                    self.calc_display.display_txt.setText(self.calc_display.display_txt.text() + text)

            else:
                if len(self.calc_display.display_txt.text()) >= 8 and text != "." and self.lines == 1:
                    self.calc_display.display_txt.setText(self.calc_display.display_txt.text() + "\n" + text)
                    self.lines += 1
                else:
                    self.calc_display.display_txt.setText(self.calc_display.display_txt.text() + text)
        else:
            self.clear_display = True
            self.calc_display.display_txt.setText(text)

    def del_char(self):
        self.calc_display.display_txt.setText(self.calc_display.display_txt.text()[:-1])
        self.lines = 2 if len(self.calc_display.display_txt.text()) > 8 else 1