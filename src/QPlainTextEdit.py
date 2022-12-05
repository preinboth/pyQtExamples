import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPlainTextEdit


class ExampleWindow(QMainWindow):
    """
    QPlainTextEdit
    """

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("PyQt6 Textarea example")

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("You can write text here.\n")
        self.b.move(10, 10)
        self.b.resize(400, 200)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit(app.exec())
