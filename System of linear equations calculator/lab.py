import sys
from PyQt5 import QtWidgets
import design
import dialog_window
import random
import dialog_window_eps
import gauss
import time
import matplotlib.pyplot as plt
import numpy as np
import copy

checkboxesStatus = {'Gauss': False, 'Kramer': False, 'Jacobi': False, 'Seidel': False, 'Unnamed': False}
MAX_SIZE_RANDOM = 100

class Dialog(QtWidgets.QDialog, dialog_window.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.answer
        self.plainTextEdit.setReadOnly(True)
        # self.answer = 'heheehehe'
        self.answer = 'heheehehe' + "\n" + "lakjsdhflkjahwsdflkj"
        # self.lineEdit.setText(self.answer)

    def startCalculation(self, A, B, extra):
        res = "Method not found"
        self.plainTextEdit.appendPlainText("Size: " + str(len(A)*2))
        if checkboxesStatus['Gauss']:
            print(A, B)
            start_time = time.time()
            res = gauss.Gauss(A, B)
            calc_time = time.time() - start_time
            print("Answer", res)
            [self.plainTextEdit.appendPlainText(str(tmp)) for tmp in res]
        # self.answer = "".join([str(tmp)+"\n" for tmp in res])
        [self.plainTextEdit.appendPlainText(str(tmp)) for tmp in res]
        # self.plainTextEdit.setText(self.answer)
        # pass
        return calc_time

class DialogAskEps(QtWidgets.QDialog, dialog_window_eps.Ui_Dialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedSize(168, 85)
        self.setupUi(self)
        self.lineEdit.setPlaceholderText('Введите значение эпсилон')

        # BUTTON ACTIONS
        self.pushButton.clicked.connect(self.takeEps)

    def takeEps(self):
        self.eps = int(self.lineEdit.text())
        print(self.eps)
        self.hide()



class CalculatorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.matrixSize_n = None
        self.matrixSize_m = None
        self.matrixOdds = None
        self.matrix = None
        self.column_vector = None
        self.matrix_list = []
        self.column_vector_list = []
        self.eps = None
        self.setupUi(self)

        # HINT FOR TYPING
        self.lineEdit.setPlaceholderText('Введите размер матрицы m*n через запятую')
        self.lineEdit_2.setPlaceholderText('Введите коэффициенты матрицы через запятую')
        self.lineEdit_3.setPlaceholderText('Введите вектор b, размер = n')

        # CHECKBOXES TRIGGERS ZONE
        self.checkBox.stateChanged.connect(lambda:self.changeCheckBoxStatus('Gauss', self.checkBox))
        self.checkBox_2.stateChanged.connect(lambda:self.changeCheckBoxStatus('Kramer', self.checkBox_2))
        self.checkBox_3.stateChanged.connect(lambda:self.changeCheckBoxStatus('Jacobi', self.checkBox_3))
        self.checkBox_4.stateChanged.connect(lambda:self.changeCheckBoxStatus('Seidel', self.checkBox_4))
        self.checkBox_5.stateChanged.connect(lambda:self.changeCheckBoxStatus('Unnamed', self.checkBox_5))
        self.dialog_eps = DialogAskEps(self)

        # BUTTONS
        self.pushButton.clicked.connect(self.OpenDialogAnswer)
        self.pushButton_3.clicked.connect(self.GetVariables)
        self.pushButton_2.clicked.connect(self.randomDifferentSize)
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

        print('n = ', self.matrixSize_n, 'm = ', self.matrixSize_m)
        print('MATRIX:')
        print(self.matrix)
        print('b = ', self.column_vector)

    def randomDifferentSize(self):
        for i in range(1, MAX_SIZE_RANDOM):
            self.randomVariables(i)
            self.matrix_list.append(copy.deepcopy(self.matrix))
            self.column_vector_list.append(copy.deepcopy(self.column_vector))
            # calc_time = self.dialog.startCalculation(self.matrix, self.column_vector, [])
            # calc_time_list.append(calc_time)
        # Data for plotting
        # t = np.array(size)
        # s = np.array(calc_time_list)
        # print(t, s)
        # fig, ax = plt.subplots()
        # ax.plot(t, s)
        #
        # ax.set(xlabel='size', ylabel='Time (s)')
        # ax.grid()
        #
        # # fig.savefig("test.png")
        # plt.show()

    def randomVariables(self, size=None):
        # self.matrixSize_n = random.randint(1, MAX_SIZE_RANDOM)
        if size is None:
            self.matrixSize_n = self.matrixSize_m = random.randint(2, MAX_SIZE_RANDOM)
        else:
            self.matrixSize_n = self.matrixSize_m = size
        self.matrix = list()

        for i in range(self.matrixSize_n):
            self.matrix.append(list())

        self.count = 0

        for i in range(self.matrixSize_n):
            for j in range(self.matrixSize_m):
                self.matrix[i].append(random.random() * MAX_SIZE_RANDOM)
                self.count += 1

        self.column_vector = [random.random() * MAX_SIZE_RANDOM for i in range(self.matrixSize_n)]

        print('n = ', self.matrixSize_n, 'm = ', self.matrixSize_m)
        print('MATRIX:')
        print(self.matrix)
        print('b = ', self.column_vector)

    def OpenDialogAnswer(self):
        calc_time_list = []
        size = [len(mat)*2 for mat in self.matrix_list]
        if len(self.matrix_list) != 0:
            for i in range(len(self.matrix_list)):
                calc_time = self.dialog.startCalculation(self.matrix_list[i], self.column_vector_list[i], [])
                calc_time_list.append(calc_time)

        self.dialog.show()
        t = np.array(size)
        s = np.array(calc_time_list)
        print(t, s)
        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='size', ylabel='Time (s)')
        ax.grid()

        # fig.savefig("test.png")
        plt.show()

    def OpenDialogAskEps(self):
        self.dialog_eps.show()

    def changeCheckBoxStatus(self, key, cb):
        if cb.isChecked():
            checkboxesStatus[key] = True
            print(checkboxesStatus)
        else:
            checkboxesStatus[key] = False
            print(checkboxesStatus)

    # def countAnswer(self):



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()