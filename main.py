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
        ln1 = self.text1.toPlainText().replace(' ', '').replace('\n', '').replace('\t', '')
        ln2 = self.text2.toPlainText().replace(' ', '').replace('\n', '').replace('\t', '')
        for i in range(min(len(ln1), len(ln2))):
            if ln1[i] == ln2[i]:
                cou += 1
        mx = max(len(ln1), len(ln2))
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
