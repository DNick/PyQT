# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.red = QtWidgets.QPushButton(self.centralwidget)
        self.red.setObjectName("red")
        self.color = QtWidgets.QButtonGroup(MainWindow)
        self.color.setObjectName("color")
        self.color.addButton(self.red)
        self.verticalLayout_2.addWidget(self.red)
        self.green = QtWidgets.QPushButton(self.centralwidget)
        self.green.setObjectName("green")
        self.color.addButton(self.green)
        self.verticalLayout_2.addWidget(self.green)
        self.blue = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blue.sizePolicy().hasHeightForWidth())
        self.blue.setSizePolicy(sizePolicy)
        self.blue.setObjectName("blue")
        self.color.addButton(self.blue)
        self.verticalLayout_2.addWidget(self.blue)
        self.all = QtWidgets.QPushButton(self.centralwidget)
        self.all.setObjectName("all")
        self.color.addButton(self.all)
        self.verticalLayout_2.addWidget(self.all)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vs = QtWidgets.QPushButton(self.centralwidget)
        self.vs.setObjectName("vs")
        self.rotate = QtWidgets.QButtonGroup(MainWindow)
        self.rotate.setObjectName("rotate")
        self.rotate.addButton(self.vs)
        self.horizontalLayout.addWidget(self.vs)
        self.for_2 = QtWidgets.QPushButton(self.centralwidget)
        self.for_2.setObjectName("for_2")
        self.rotate.addButton(self.for_2)
        self.horizontalLayout.addWidget(self.for_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red.setText(_translate("MainWindow", "R"))
        self.green.setText(_translate("MainWindow", "G"))
        self.blue.setText(_translate("MainWindow", "B"))
        self.all.setText(_translate("MainWindow", "ALL"))
        self.vs.setText(_translate("MainWindow", "Против часовой стрелки"))
        self.for_2.setText(_translate("MainWindow", "По часовой стрелке"))
