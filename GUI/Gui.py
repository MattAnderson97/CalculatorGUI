from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtGui import QIcon

from GUI.MainLayout import MainLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        # self.setWindowFlags(Qt.FramelessWindowHint)

        self.main_layout = MainLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # self.main_layout.window_bar.close_btn.clicked.connect(self.close)
        # self.main_layout.window_bar.minimise_btn.clicked.connect(self.showMinimized)
        # self.main_layout.window_bar.maximise_btn.clicked.connect(self.showMaximized)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)
