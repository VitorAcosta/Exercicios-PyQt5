# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\ex1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnInc = QtWidgets.QPushButton(self.centralwidget)
        self.btnInc.setGeometry(QtCore.QRect(60, 40, 171, 61))
        self.btnInc.setObjectName("btnInc")
        self.lblValor = QtWidgets.QLabel(self.centralwidget)
        self.lblValor.setGeometry(QtCore.QRect(100, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lblValor.setFont(font)
        self.lblValor.setAlignment(QtCore.Qt.AlignCenter)
        self.lblValor.setObjectName("lblValor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
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
        self.btnInc.setText(_translate("MainWindow", "Clique para incrementar"))
        self.lblValor.setText(_translate("MainWindow", "0"))

