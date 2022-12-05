import sys

from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Demo Radiobutton")

        radio = QRadioButton("Option 1", self)
        radio.move(100, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
