import sys

from PyQt6.QtWidgets import QApplication, QWidget, QProgressBar


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 250)
        self.setWindowTitle("CodersLegacy")

        prog_bar = QProgressBar(self)
        prog_bar.setGeometry(50, 100, 250, 30)
        prog_bar.setValue(0)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
