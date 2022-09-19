import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QLCDNumber, QMainWindow
from ui.anti import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.compare)

    def compare(self):
        cou = 0
        for i in range(min(len(self.plainTextEdit.toPlainText()), len(self.plainTextEdit_2.toPlainText()))):
            if self.plainTextEdit.toPlainText()[i] == self.plainTextEdit_2.toPlainText()[i]:
                cou += 1
        mx = max(len(self.plainTextEdit.toPlainText()), len(self.plainTextEdit_2.toPlainText()))
        if mx:
            self.statusbar.showMessage(f'Код похож на {round(cou * 100 / mx, 2)}%')
            if cou * 100 / mx > float(self.doubleSpinBox.text().replace(',', '.')):
                self.statusbar.setStyleSheet('background-color : red')
            else:
                self.statusbar.setStyleSheet('background-color : green')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
