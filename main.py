import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QLCDNumber, QMainWindow
from ui.calc import Ui_Form
from math import factorial

class Example(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.buttonGroup_digits.buttonClicked.connect(self.number)
        self.buttonGroup_binary.buttonClicked.connect(self.binary)
        self.action = 'calm'
        self.btn_eq.clicked.connect(self.equal)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)
        self.btn_clear.clicked.connect(self.clear)

    def number(self, button):
        if self.table.intValue() == 'Error':
            return
        if self.action == 'calm':
            if self.table.intValue() == 0:
                self.table.display(button.text())
            elif self.table.value() % 1 == 0:
                self.table.display(str(self.table.value())[:-1] + button.text())
            else:
                self.table.display(str(self.table.value()) + button.text())
        else:
            self.table.display(int(button.text()))
            self.action = 'calm'

    def binary(self, button):
        if self.table.intValue() == 'Error':
            return
        self.action = 'binary'
        if button.text() == '^':
            self.vir = str(self.table.value()) + '**'
        else:
            self.vir = str(self.table.value()) + button.text()

    def equal(self):
        if self.table.intValue() == 0 and self.vir[-1] == '/':
            self.table.display('Error')
        else:
            self.table.display(eval(self.vir + str(self.table.intValue())))
            self.action = 'after_eq'

    def sqrt(self):
        if self.table.value() >= 0:
            self.table.display(self.table.value() ** 0.5)
        else:
            self.table.display('Error')

    def fact(self):
        if self.table.value() % 1 == 0:
            self.table.display(factorial(self.table.value()))
        else:
            self.table.display('Error')

    def dot(self):
        self.table.display(str(self.table.intValue()) + '.')

    def clear(self):
        self.table.display(0)
        self.action = 'calm'
        self.vir = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
