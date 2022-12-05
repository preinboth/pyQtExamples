import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 SpreadSheet")
        self.resize(400, 250)
        self.CreateTable()
        self.show()

    def CreateTable(self):
        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Name", "Age", "Gender"])

        self.table.setItem(0, 0, QTableWidgetItem("Oz"))
        self.table.setItem(0, 1, QTableWidgetItem("14"))
        self.table.setItem(0, 2, QTableWidgetItem("Male"))
        self.table.setColumnWidth(0, 150)

        self.table.setItem(1, 0, QTableWidgetItem("John"))
        self.table.setItem(1, 1, QTableWidgetItem("24"))
        self.table.setItem(1, 2, QTableWidgetItem("Male"))

        self.table.setItem(2, 0, QTableWidgetItem("Lucy"))
        self.table.setItem(2, 1, QTableWidgetItem("19"))
        self.table.setItem(2, 2, QTableWidgetItem("Female"))

        self.table.setItem(3, 0, QTableWidgetItem("Subaru"))
        self.table.setItem(3, 1, QTableWidgetItem("18"))
        self.table.setItem(3, 2, QTableWidgetItem("Male"))

        self.table.setItem(4, 0, QTableWidgetItem("William"))
        self.table.setItem(4, 1, QTableWidgetItem("60"))
        self.table.setItem(4, 2, QTableWidgetItem("Male"))

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
