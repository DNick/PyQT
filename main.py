import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from ui.flag import Ui_mainWindow


class Example(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.do)

    def do(self):
        a, b = self.buttonGroup.checkedButton().text(), self.buttonGroup_2.checkedButton().text()
        c = self.buttonGroup_3.checkedButton().text()
        self.label_4.setText(f"Цвета: {a}, {b} и {c}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
