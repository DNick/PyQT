import sys

from PIL.Image import Transpose
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QCheckBox, QLCDNumber, QMainWindow
from ui.interface import Ui_MainWindow
from PIL import Image


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def set_image(self, name):
        self.pixmap = QPixmap(name).scaled(600, 500)
        self.label = QLabel('')
        self.label.setPixmap(self.pixmap)

    def initUI(self):
        uic.loadUi('ui/interface.ui', self)
        self.setWindowTitle('PIL 2.0')
        self.rotat = 0
        Image.open('based.png').save('changed.png')
        self.set_image('changed.png')
        self.verticalLayout_3.addWidget(self.label)
        self.color.buttonClicked.connect(self.change_color)
        self.rotate.buttonClicked.connect(self.rotates)

    def rotates(self, button: QPushButton):
        if button.objectName() == 'vs':
            Image.open('changed.png').transpose(Transpose.ROTATE_90).save('changed.png')
            self.rotat += 1
        else:
            Image.open('changed.png').transpose(Transpose.ROTATE_270).save('changed.png')
            self.rotat += 3

        label = self.label
        self.set_image("changed.png")
        self.verticalLayout_3.replaceWidget(label, self.label)

    def change_color(self, button: QPushButton):
        if button.text() == 'R':
            colors = [1, 0, 0]
        elif button.text() == 'G':
            colors = [0, 1, 0]
        elif button.text() == 'B':
            colors = [0, 0, 1]
        else:
            colors = [1, 1, 1]

        im = Image.open("based.png")
        for i in range(self.rotat):
            im = im.transpose(Transpose.ROTATE_90)
        pixels = im.load()
        x, y = im.size

        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                pixels[i, j] = r * colors[0], g * colors[1], b * colors[2]
        im.save('changed.png')
        label = self.label
        self.set_image("changed.png")
        self.verticalLayout_3.replaceWidget(label, self.label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
