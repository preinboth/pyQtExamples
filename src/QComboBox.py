import sys

from PyQt6.QtWidgets import QApplication, QWidget, QComboBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("CodersLegacy")

        combo = QComboBox(self)
        combo.addItem("Python")
        combo.addItem("Java")
        combo.addItem("C++")
        combo.move(100, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
