# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

# Поля внутри строки разделены точкой с запятой, оценки — целые числа.

# Напишите программу, которая считывает исходный файл с подобной структурой и для каждого абитуриента записывает его среднюю оценку 
# по трём предметам на отдельной строке, соответствующей этому абитуриенту, в файл с ответом.

# Также вычислите средние баллы по математике, физике и русскому языку по всем абитуриентам и добавьте полученные значения, 
# разделённые пробелом, последней строкой в файл с ответом.

# В качестве ответа на задание прикрепите полученный файл со средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.

math_marks = []
physics_marks = []
russian_marks = []

round_number = 9

with open("dataset_3363_4.txt") as inf:
    for line in inf:
        curr_line = line.strip().split(';')
        math_marks.append(int(curr_line[1]))
        physics_marks.append(int(curr_line[2]))
        russian_marks.append(int(curr_line[3]))

with open("output.txt", 'w') as outf:
    for i in range(len(math_marks)):
        outf.write(str(round((math_marks[i] + physics_marks[i] + russian_marks[i]) / 3, round_number)) + '\n')
    outf.write(str(round(sum(math_marks) / len(math_marks), round_number)) + ' ' + str(round(sum(physics_marks) / len(physics_marks), round_number)) + ' ' + str(round(sum(russian_marks) / len(russian_marks), round_number)))




