import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from ui.interface import Ui_MainWindow


class DBSample(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/interface.ui', self)
        self.connection = sqlite3.connect("films_db.sqlite")
        for i in self.connection.cursor().execute('SELECT genres.title from genres').fetchall():
            self.comboBox.addItem(i[0])
        self.pushButton.clicked.connect(self.select_data)

    def select_data(self):
        text = self.comboBox.currentText()
        query = f'''SELECT films.title, films.genre, films.year 
        FROM films, genres WHERE films.genre = genres.id AND genres.title = "{text}"'''
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Название", "Жанр", "Год"])
        for i in range(len(res)):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j in range(3):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(res[i][j])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
