import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ex7 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.mostraMsg)

    def mostraMsg(self):
        if self.ui.checkBox.isChecked(): #Verifica o estado do checkbox.
            #Mostra mensagem de erro
            Msg = QMessageBox()
            Msg.setWindowTitle("ERRO")
            Msg.setIcon(QMessageBox.Critical)
            Msg.setText("Você digitou:" + self.ui.txtMsg.text())
            retorno = Msg.exec()
        else:
            Msg = QMessageBox()
            Msg.setWindowTitle("Informação")
            Msg.setIcon(QMessageBox.Information)
            Msg.setText(self.ui.txtMsg.text())
            retorno = Msg.exec()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


