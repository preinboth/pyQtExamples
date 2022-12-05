import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 200))
        self.setWindowTitle("PyQt messagebox example")

        pybutton = QPushButton('Show messagebox', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 64)
        pybutton.move(50, 50)

    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
