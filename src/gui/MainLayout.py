import re

from src.gui.CalcButtons import CalcButtons
from src.gui.CalcDisplay import CalcDisplay
from PyQt5.QtWidgets import QVBoxLayout


class MainLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        # self.window_bar = WindowBar()
        self.calc_display = CalcDisplay()
        self.calc_buttons = CalcButtons()

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

    def update_display(self, text, result):
        if not result:
            if self.calc_display.display_txt.text() == "0":
                if re.match(r'^[0-9]*$', text):
                    self.calc_display.display_txt.setText(text)
                else:
                    self.calc_display.display_txt.setText(self.calc_display.display_txt.text() + text)
            else:
                self.calc_display.display_txt.setText(self.calc_display.display_txt.text() + text)
        else:
            self.calc_display.display_txt.setText(text)