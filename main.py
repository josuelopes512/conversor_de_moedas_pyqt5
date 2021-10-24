import sys
from app import *

class App(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.lineEdit.textChanged.connect(self.converter)
        self.pushButton.clicked.connect(self.inverter)

    
    def inverter(self):
        # self.pushButton
        a = self.comboBox.currentIndex()
        b = self.comboBox_2.currentIndex()
        self.comboBox.setCurrentIndex(b)
        self.comboBox_2.setCurrentIndex(a)

    def converter(self):
        valor = float(self.lineEdit.text()) if self.lineEdit.text() else None
        convertido = api.conversor(
            self.comboBox.currentText(), self.comboBox_2.currentText(), valor
        ) if valor else ""
        self.lineEdit_2.setText("{}".format(convertido))
        if api.moeda():
            self.label_3.setText(
                "      1 {} = {} {}".format(
                    self.comboBox.currentText(), api.moeda(), self.comboBox_2.currentText()))
        return self.lineEdit_2.paste

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    layout = App()
    layout.show()
    sys.exit(app.exec_())