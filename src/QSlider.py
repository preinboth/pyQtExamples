import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QSlider


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Slider Demo")

        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setGeometry(50, 50, 200, 50)
        slider.setMinimum(0)
        slider.setMaximum(20)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.setTickInterval(2)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
