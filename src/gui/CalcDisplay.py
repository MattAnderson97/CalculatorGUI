from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QColor


class CalcDisplay(QWidget):
    def __init__(self):
        super().__init__()

        self.display_txt = QLabel("0")
        self.display_txt.setStyleSheet("font-size: 35px; color: white; font-weight: 500;")
        self.display_layout = QVBoxLayout()
        self.display_layout.addWidget(self.display_txt)

        self.setLayout(self.display_layout)
        self.setMinimumHeight(75)

        self.setAutoFillBackground(True)
        display_palette = self.palette()
        display_palette.setColor(self.backgroundRole(), QColor(30, 30, 30))
        self.setPalette(display_palette)
