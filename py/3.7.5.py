# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

# Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост

# Класс обозначается только числом. Буквенные модификаторы не используются. Номер класса может быть от 1 до 11 включительно. 
# В фамилии нет пробелов, а в качестве роста используется натуральное число, но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

# Выводить информацию о среднем росте следует в порядке возрастания номера класса (для классов с первого по одиннадцатый). 
# Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.

# В качестве ответа прикрепите файл с полученными данными о среднем росте.

class_data = {k: [] for k in range(1, 12)}

def avg_height(a):
    sum = 0
    count = 0
    for i in a:
        sum += i
        count += 1
    return float(sum / count)

with open("dataset_3380_5.txt") as inf:
    for line in inf:
        curr_line = line.strip().split()
        if len(curr_line) == 0:
            break
        class_num = int(curr_line[0])
        height = int(curr_line[2])
        class_data[class_num].append(height)

for key, value in class_data.items():
    if len(class_data[key]) != 0:
        print(key,avg_height(class_data[key]), sep =' ')
    else:
        print(key, '-', sep=' ')