from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from src.gui.OpBtn import OpBtn


class CalcDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(140)

        self.display_txt = QLabel("0")
        self.btn_clr = OpBtn("CE")
        self.btn_back = OpBtn("←")

        self.btn_layout = QVBoxLayout()
        self.btn_layout.addWidget(self.btn_clr, alignment=Qt.AlignRight)
        self.btn_layout.addWidget(self.btn_back, alignment=Qt.AlignRight)

        self.btns = QWidget()
        self.btns.setLayout(self.btn_layout)

        self.display_txt.setStyleSheet("font-size: 35px; color: white; font-weight: 500;")
        self.display_layout = QHBoxLayout()
        self.display_layout.addWidget(self.display_txt, Qt.AlignLeft)
        self.display_layout.addWidget(self.btns, Qt.AlignRight)

        self.setLayout(self.display_layout)
        self.setMinimumHeight(75)

        self.setAutoFillBackground(True)
        display_palette = self.palette()
        display_palette.setColor(self.backgroundRole(), QColor(30, 30, 30))
        self.setPalette(display_palette)

        self.btn_clr.clicked.connect(lambda: self.display_txt.setText("0"))
