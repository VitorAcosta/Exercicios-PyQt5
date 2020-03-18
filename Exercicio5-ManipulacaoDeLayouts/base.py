import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ex5 import *


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.printaDados)

    def printaDados(self):
        print("Nome: {}\nTelefone:{}"
              .format(self.ui.txtNome.text(), self.ui.txtTel.text()))
        #Note que você pode usar tanto o SetText como ""
        #ou o método clear do QLineEdit para limpar o campo.
        self.ui.txtNome.setText("")
        self.ui.txtTel.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
    


