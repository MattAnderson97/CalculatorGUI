import ctypes
import sys

from PyQt5.QtWidgets import QApplication

from GUI.Gui import MainWindow


if __name__ == "__main__":
    # sets task bar icon
    # https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
    appid = 'space.wolv.calculator.1-0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

    # launch application
    application = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.raise_()
    application.exec_()