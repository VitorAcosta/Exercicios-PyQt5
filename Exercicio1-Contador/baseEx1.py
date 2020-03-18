import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex1 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        #Instancia da classe Ui_MainWindow, que é a classe que contém todas
        #informações da interface.
        self.ui = Ui_MainWindow()

        #Chama-se o método setupUi e passando o self como argumento.
        self.ui.setupUi(self)

        #Signal de clique no botão, que ativa um método criado por nós.
        self.ui.btnInc.clicked.connect(self.incrementa)

    def incrementa(self):
        #Adquirimos o texto que está no label, e convertemos para int, a
        #fim de incrementar esse valor, se não fosse feita a conversão,
        #não conseguiriamos descrever o comportamento "valor + 1"
        valor = int(self.ui.lblValor.text())

        #Definimos o valor incrementado como o texto da label,
        #e aqui convertemos o valor em Int para String.
        self.ui.lblValor.setText(str(valor + 1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


