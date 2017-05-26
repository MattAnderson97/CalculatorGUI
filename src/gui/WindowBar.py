from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
        """)


class WindowBar(QWidget):
    def __init__(self):
        super().__init__()
        self.close_btn = QPushButton("x")
        self.close_btn.setStyleSheet("""
        background: #ff5c5c;
        font-size: 8px;
        padding-bottom: 2px;
        border: 1px solid #e33e41;
        border-radius:5px;
        """)
        self.close_btn.setFixedHeight(10)
        self.close_btn.setFixedWidth(10)

        self.minimise_btn = QPushButton("-")
        self.minimise_btn.setStyleSheet("""
        background: #ffbd4c;
        font-size: 8px;
        padding-bottom: 2px;
        border: 1px solid #e09e3e;
        border-radius:5px;
        self.minimise_btn.setFixedHeight(10)
        self.minimise_btn.setFixedWidth(10)

        self.maximise_btn = QPushButton("+")
        self.maximise_btn.setStyleSheet("""
        background: #00ca56;
        font-size: 8px;
        padding-bottom: 2px;
        border: 1px solid #14ae46;
        border-radius:5px;
        """)
        self.maximise_btn.setFixedHeight(10)
        self.maximise_btn.setFixedWidth(10)

        self.window_bar = QHBoxLayout()

        self.window_bar.addWidget(self.close_btn, Qt.AlignLeft, Qt.AlignTop)
        self.window_bar.addWidget(self.minimise_btn, Qt.AlignLeft, Qt.AlignTop)
        self.window_bar.addWidget(self.maximise_btn, Qt.AlignLeft, Qt.AlignTop)

        self.setContentsMargins(3, 3, 3, 3)
        self.setAlignment(Qt.AlignTop)

        self.setLayout(self.window_bar)

        self.setAutoFillBackground(True)
        window_bar_palette = self.palette()
        window_bar_palette.setColor(self.window_bar_widget.backgroundRole(), QColor(185, 185, 185))
        self.setPalette(window_bar_palette)
        self.setFixedHeight(20)