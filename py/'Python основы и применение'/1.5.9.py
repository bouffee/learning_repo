# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.
#
# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
#
# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок последовательных элементов по мере их накопления.
#
# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно необходимо, т. е. он не должен хранить элементы,
# которые уже вошли в пятерку, для которой была выведена сумма.


class Buffer:
    def __init__(self): #конструктор без аргументов
        self.buffer = list()
        self.sum = 0
        self.sum_prev = 0

    def add(self, *a): #добавить следующую часть последовательности
        for i in a:
            self.buffer.append(i)
            if len(self.buffer) == 5:
                for j in self.buffer[0:5]:
                    self.sum += j
                del self.buffer[:5]
                self.sum_prev = self.sum
                self.sum = 0
                print(self.sum_prev, end ='\n')

    def get_current_part(self): #вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.buffer

#test

buf = Buffer()
buf.add(1, 2, 3)
x = buf.get_current_part()
print("current list:", x) #x = [1, 2, 3]
buf.add(4, 5, 6) #print current sum of 5 elementsof the list: 15
x = buf.get_current_part()
print("current list:", x) #x = [6]
buf.add(7, 8, 9, 10) #print sum of next 5 elements in the list: 40
x = buf.get_current_part()
print("current list:", x) #x = []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) #print sum of 3rd and 4th 5 elements of the list: 5 and 5
x = buf.get_current_part()
print("current list:", x) #x =[1]