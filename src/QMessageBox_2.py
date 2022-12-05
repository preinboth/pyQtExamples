import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("Demo MessageBox")

        dialog = QMessageBox(parent=self, text="Hello World")
        dialog.setWindowTitle("Message Dialog")
        ret = dialog.exec()  # Stores the return value for the button pressed


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
