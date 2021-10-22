import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from app import *

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Tela()
    ui.show()
    sys.exit(app.exec_())