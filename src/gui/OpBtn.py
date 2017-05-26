from PyQt5.QtWidgets import QPushButton

class OpBtn(QPushButton):
    def __init__(self, text=""):
        super().__init__(text)
        self.setMinimumHeight(45)
        self.setMinimumWidth(45)
        self.setStyleSheet("""
        background-color: rgb(60, 60, 60);
        border: 1px solid rgb(60, 60, 60);
        border-radius 20px;
        font-size: 32px;
        font-weight: 500;
        color: #ccc;
        """)