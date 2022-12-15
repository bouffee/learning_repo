import sys
from PyQt5 import QtWidgets
import design
import dialog_window
import random

checkboxesStatus = {'Gauss': False, 'Kramer': False, 'Jacobi': False, 'Seidel': False, 'Unnamed': False}
MAX_SIZE_RANDOM = 10

class Dialog(QtWidgets.QDialog, dialog_window.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class CalculatorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # CHECKBOXES TRIGGERS ZONE
        self.checkBox.stateChanged.connect(lambda:self.changeCheckBoxStatus('Gauss', self.checkBox))
        self.checkBox_2.stateChanged.connect(lambda:self.changeCheckBoxStatus('Kramer', self.checkBox_2))
        self.checkBox_3.stateChanged.connect(lambda:self.changeCheckBoxStatus('Jacobi', self.checkBox_3))
        self.checkBox_4.stateChanged.connect(lambda:self.changeCheckBoxStatus('Seidel', self.checkBox_4))
        self.checkBox_5.stateChanged.connect(lambda:self.changeCheckBoxStatus('Unnamed', self.checkBox_5))

        # BUTTONS
        self.pushButton.clicked.connect(self.OpenDialog)
        self.pushButton_3.clicked.connect(self.GetVariables)
        self.pushButton_2.clicked.connect(self.randomVariables)
        self.dialog = Dialog(self)


    def GetVariables(self):
        # SIZE OF MATRIX, m - WEIGHT, n - HEIGHT
        self.inp = list()
        self.inp = self.lineEdit.text().strip().split(',')
        self.matrixSize_n = int(self.inp[1])
        self.matrixSize_m = int(self.inp[0])
        self.matrixOdds = self.lineEdit_2.text().strip().split(',')

        # MAKE A 2D ARRAY FROM A LIST
        self.matrix = list()

        for i in range(self.matrixSize_n):
            self.matrix.append(list())

        self.count = 0
        for i in range(self.matrixSize_n):
            for j in range(self.matrixSize_m):
                self.matrix[i].append(self.matrixOdds[self.count])
                self.count += 1

        # INITIALIZATION OF COLUMN VECTOR b
        self.column_vector = self.lineEdit_3.text().strip().split(',')

        # print('n = ', self.matrixSize_n, 'm = ', self.matrixSize_m)
        # print('MATRIX:')
        # print(self.matrix)
        # print('b = ', self.column_vector)

    def randomVariables(self):
        self.matrixSize_n = random.randint(1, MAX_SIZE_RANDOM)
        self.matrixSize_m = random.randint(1, MAX_SIZE_RANDOM)
        self.matrix = list()

        for i in range(self.matrixSize_n):
            self.matrix.append(list())

        self.count = 0

        for i in range(self.matrixSize_n):
            for j in range(self.matrixSize_m):
                self.matrix[i].append(random.random() * MAX_SIZE_RANDOM)
                self.count += 1

        self.column_vector = [random.random() * MAX_SIZE_RANDOM for i in range(self.matrixSize_n)]

        # print('n = ', self.matrixSize_n, 'm = ', self.matrixSize_m)
        # print('MATRIX:')
        # print(self.matrix)
        # print('b = ', self.column_vector)

    def OpenDialog(self):
        self.dialog.show()

    def changeCheckBoxStatus(self, key, cb):
        if cb.isChecked():
            checkboxesStatus[key] = True
            print(checkboxesStatus)
        else:
            checkboxesStatus[key] = False
            print(checkboxesStatus)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()