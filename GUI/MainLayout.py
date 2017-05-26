from PyQt5.QtWidgets import QVBoxLayout

from GUI.CalcButtons import CalcButtons
from GUI.CalcDisplay import CalcDisplay
from GUI.WindowBar import WindowBar


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
