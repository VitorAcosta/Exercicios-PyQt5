import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex2 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        #Instancia da classe Ui_MainWindow, que é a classe que contém todas
        #informações da interface.
        self.ui = Ui_MainWindow()

        #Chama-se o método setupUi e passando o self como argumento.
        self.ui.setupUi(self)

        #Signal de clique no botão, que ativa um método criado por nós.
        self.ui.pushButton.clicked.connect(self.mensagem)

    def mensagem(self):
        #Define-se o texto do Label como sendo a string "Olá" +
        #o conteudo escrito no QLineEdit.
        self.ui.lblSaida.setText("Olá {}".format(self.ui.txtNome.text()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


