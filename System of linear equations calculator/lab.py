import sys
from PyQt5 import QtWidgets
import design
import dialog_window

checkboxesStatus = {'Gauss': False, 'Kramer': False, 'Jacobi': False, 'Seidel': False, 'Unnamed': False}


class Dialog(QtWidgets.QDialog, dialog_window.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class CalculatorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def changeCheckBoxStatus(self, key, cb):
        if cb.isChecked():
            checkboxesStatus[key] = True
            print(checkboxesStatus)
        else:
            checkboxesStatus[key] = False
            print(checkboxesStatus)

    def OpenDialog(self):
        self.dialog.show()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.OpenDialog)
        self.dialog = Dialog(self)

        # CHECKBOXES TRIGGERS ZONE
        self.checkBox.stateChanged.connect(lambda:self.changeCheckBoxStatus('Gauss', self.checkBox))
        self.checkBox_2.stateChanged.connect(lambda:self.changeCheckBoxStatus('Kramer', self.checkBox_2))
        self.checkBox_3.stateChanged.connect(lambda:self.changeCheckBoxStatus('Jacobi', self.checkBox_3))
        self.checkBox_4.stateChanged.connect(lambda:self.changeCheckBoxStatus('Seidel', self.checkBox_4))
        self.checkBox_5.stateChanged.connect(lambda:self.changeCheckBoxStatus('Unnamed', self.checkBox_5))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()