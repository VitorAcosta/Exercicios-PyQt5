# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\SAMSUNG\Desktop\ex3.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 225)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 47, 13))
        self.label.setObjectName("label")
        self.txtV1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtV1.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.txtV1.setObjectName("txtV1")
        self.txtV2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtV2.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.txtV2.setObjectName("txtV2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 61, 21))
        self.label_3.setObjectName("label_3")
        self.txtResultado = QtWidgets.QLineEdit(self.centralwidget)
        self.txtResultado.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.txtResultado.setReadOnly(True)
        self.txtResultado.setObjectName("txtResultado")
        self.btnAdicao = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdicao.setGeometry(QtCore.QRect(260, 20, 41, 41))
        self.btnAdicao.setObjectName("btnAdicao")
        self.btnMul = QtWidgets.QPushButton(self.centralwidget)
        self.btnMul.setGeometry(QtCore.QRect(260, 70, 41, 41))
        self.btnMul.setObjectName("btnMul")
        self.btnSub = QtWidgets.QPushButton(self.centralwidget)
        self.btnSub.setGeometry(QtCore.QRect(310, 20, 41, 41))
        self.btnSub.setObjectName("btnSub")
        self.btnDiv = QtWidgets.QPushButton(self.centralwidget)
        self.btnDiv.setGeometry(QtCore.QRect(310, 70, 41, 41))
        self.btnDiv.setObjectName("btnDiv")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
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
        self.label.setText(_translate("MainWindow", "Valor 1:"))
        self.label_2.setText(_translate("MainWindow", "Valor 2:"))
        self.label_3.setText(_translate("MainWindow", "Resultado:"))
        self.btnAdicao.setText(_translate("MainWindow", "+"))
        self.btnMul.setText(_translate("MainWindow", "*"))
        self.btnSub.setText(_translate("MainWindow", "-"))
        self.btnDiv.setText(_translate("MainWindow", "/"))
