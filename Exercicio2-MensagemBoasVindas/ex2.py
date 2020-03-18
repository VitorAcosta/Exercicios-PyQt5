# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\ex2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 91, 16))
        self.label.setObjectName("label")
        self.txtNome = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNome.setGeometry(QtCore.QRect(130, 40, 191, 16))
        self.txtNome.setObjectName("txtNome")
        self.lblSaida = QtWidgets.QLabel(self.centralwidget)
        self.lblSaida.setGeometry(QtCore.QRect(30, 180, 301, 21))
        self.lblSaida.setAlignment(QtCore.Qt.AlignCenter)
        self.lblSaida.setObjectName("lblSaida")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Insira seu nome:"))
        self.lblSaida.setText(_translate("MainWindow", "--"))
        self.pushButton.setText(_translate("MainWindow", "Clique aqui"))
