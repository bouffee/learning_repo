# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
#
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно положить в копилку.
# Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность добавлять монеты в копилку и узнавать,
# можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.


class MoneyBox:
    def __init__(self, capacity):
        #конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):
        #True, если можно добавить v монет, False иначе
        if self.capacity >= v:
            return True
        else:
            return False

    def add(self, v):
        #положить v монет в копилку
        if self.can_add(v):
            self.capacity -= v
            return True
        else:
            return False


#Test
pig = MoneyBox(10)
pig.add(7)
print(pig.can_add(4))
print(pig.can_add(3))
pig.add(3)
print(pig.can_add(1))
