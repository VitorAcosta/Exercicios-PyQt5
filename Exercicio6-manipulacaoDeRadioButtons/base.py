import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex6 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tamanho = None
        self.pagamento = None

        self.ui.rbP.toggled.connect(self.getTamanho)
        self.ui.rbM.toggled.connect(self.getTamanho)
        self.ui.rbG.toggled.connect(self.getTamanho)
        self.ui.rbDeb.toggled.connect(self.getPagto)
        self.ui.rbCred.toggled.connect(self.getPagto)
        self.ui.rbDin.toggled.connect(self.getPagto)

    def getTamanho(self):
        self.tamanho = self.sender().text()
        self.confirmaCompra()

    def getPagto(self):
        self.pagamento = self.sender().text()
        self.confirmaCompra()

    def confirmaCompra(self):
        if self.tamanho is not None and self.pagamento is not None:
            resposta = 'Você selecionou o tamanho: {} e a forma de pagamento: {}'.format(self.tamanho, self.pagamento)
            self.ui.lblSaida.setText(resposta)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


