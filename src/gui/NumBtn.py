from PyQt5.QtWidgets import QPushButton

class NumBtn(QPushButton):
    def __init__(self, text=""):
        super().__init__(text)
        self.setMinimumHeight(45)
        self.setStyleSheet("""
        background-color: #ccc;
        border: 1px solid #ccc;
        border-radius 20px;
        font-size: 32px;
        font-weight: 500;
        color: #333;
        """)