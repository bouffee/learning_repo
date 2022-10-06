# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две строки одинаковой длины, 
# на первой строке записаны символы исходного алфавита, на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, 
# и ещё одна строка, которую нужно расшифровать.

# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%

# Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки, которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac

decoding_dict = {}

uncoded = input()
coded = input()
for i in range(0, len(uncoded)):
    decoding_dict[uncoded[i]] = coded[i]
task_1 = input()
task_2 = input()
for i in range(0, len(task_1)):
    if i == len(task_1) - 1:
        print(decoding_dict[task_1[i]])
        break
    print(decoding_dict[task_1[i]], end="")
for i in range(0, len(task_2)):
    for key, value in decoding_dict.items():
        if value == task_2[i]:
            print(key, end="")