import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex3 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        #Instancia da classe Ui_MainWindow, que é a classe que contém todas
        #informações da interface.
        self.ui = Ui_MainWindow()

        #Chama-se o método setupUi e passando o self como argumento.
        self.ui.setupUi(self)


        #Ligando todos os botões ao mesmo método, por isso utiliza-se o lambda
        #através dessa função anônima, conseguimos passar parâmetros. 
        self.ui.btnAdicao.clicked.connect(lambda x: self.operacao("Add"))
        self.ui.btnSub.clicked.connect(lambda x: self.operacao("Sub"))
        self.ui.btnMul.clicked.connect(lambda x: self.operacao("Mul"))
        self.ui.btnDiv.clicked.connect(lambda x: self.operacao("Div"))

    def operacao(self, operador):
        
        
        #Adquire os dois valores inseridos.
        self.nmr1 = self.ui.txtV1.text()
        self.nmr2 = self.ui.txtV2.text()

        if(self.nmr1 == "" or self.nmr2 == ""):
            self.ui.txtResultado.setText("ERRO")
        else:
            if(operador == "Add"):
                self.ui.txtResultado.setText(str(int(self.nmr1) + int(self.nmr2)))
            elif(operador == "Sub"):
                self.ui.txtResultado.setText(str(int(self.nmr1) - int(self.nmr2)))
            elif(operador == "Mul"):
                self.ui.txtResultado.setText(str(int(self.nmr1) * int(self.nmr2)))
            else:
                self.ui.txtResultado.setText(str(int(self.nmr1) / int(self.nmr2)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


