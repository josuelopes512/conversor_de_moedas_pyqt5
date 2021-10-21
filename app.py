import sys
from PyQt5.QtWidgets import QDialog, QApplication
from dialog import Ui_Dialog

#  pyuic5 .\untitled.ui > dialog.py
class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())