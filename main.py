import csv
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui.interface import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/interface.ui', self)
        self.setWindowTitle('Результат олимпиады: фильтрация')
        self.comboBox_2.addItem('Все')
        self.comboBox.addItem('Все')
        self.comboBox_2.setCurrentText('Все')
        self.second()
        self.comboBox.currentIndexChanged.connect(self.first)
        self.comboBox_2.currentIndexChanged.connect(self.second)
        self.pushButton.clicked.connect(self.print)

    def first(self):
        if self.comboBox_2.currentText() != 'Все':
            return
        for i in range(self.comboBox_2.count() - 1):
            self.comboBox_2.removeItem(1)
        with open('rez.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            sp = set()
            for index, row in enumerate(reader):
                if index != 0:
                    sp.add(row[2].split('-')[3])

        self.comboBox_2.addItems(list(sp))

    def second(self):
        if self.comboBox.currentText() != 'Все':
            return
        for i in range(self.comboBox.count() - 1):
            self.comboBox.removeItem(1)
        with open('rez.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            sp = set()
            for index, row in enumerate(reader):
                if index != 0:
                    sp.add(row[2].split('-')[2])
            self.comboBox.addItems(list(sp))

    def print(self):
        a, b = self.comboBox.currentText(), self.comboBox_2.currentText()
        flag1 = False
        flag2 = False
        if a == 'Все':
            flag1 = True
            a = '0'
        if b == 'Все':
            flag2 = True
            b = '0'

        with open('rez.csv', encoding="utf8", newline='') as inp:
            reader = csv.reader(inp, delimiter=',', quotechar='"')
            sp = []
            for index, row in enumerate(reader):
                if index != 0 and (int(row[2].split('-')[2]) == int(a) or flag1) and \
                        (int(row[2].split('-')[3]) == int(b) or flag2):
                    sp.append([row[1].split()[-2], row[-1], row[1]])
            sp.sort(key=lambda x: (int(x[1]), x[0]), reverse=True)
            win3, win2, win1 = sorted(list(set(map(lambda x: int(x[1]), sp))))[-3:]
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            self.tableWidget.setHorizontalHeaderLabels(['Фамилия', "Результат", "Логин"])
            for i in range(len(sp)):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j in range(len(sp[i])):
                    item = QTableWidgetItem(sp[i][j])
                    if int(sp[i][1]) == win1:
                        item.setBackground(QColor(224, 214, 0))
                    elif int(sp[i][1]) == win2:
                        item.setBackground(QColor(180, 181, 189))
                    elif int(sp[i][1]) == win3:
                        item.setBackground(QColor(155, 82, 33))
                    self.tableWidget.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
