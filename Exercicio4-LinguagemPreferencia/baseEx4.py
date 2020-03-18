import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex4 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        #Instancia da classe Ui_MainWindow, que é a classe que contém todas
        #informações da interface.
        self.ui = Ui_MainWindow()

        #Chama-se o método setupUi e passando o self como argumento.
        self.ui.setupUi(self)

        #Signal de clique no botão, que ativa um método criado por nós.
        self.ui.pushButton.clicked.connect(self.mostraSintaxe)

    def mostraSintaxe(self):
        #Adquire-se o texto da opção escolhida pelo usuário e salva na variavel escolha.
        escolha = self.ui.comboBox.currentText()
        if(escolha == "Python"):
            self.ui.label.setText("print(“hello world”)")
        elif(escolha == "Java"):
            self.ui.label.setText("System.out.println(“Hello world”)")
        else:
            self.ui.label.setText("std::cout << “Hello world” << std::endl")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


