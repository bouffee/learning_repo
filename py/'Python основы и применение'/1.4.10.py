# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
#
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#
# Вашей программе на вход подаются следующие запросы:
#
#     create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
#     add <namespace> <var> – добавить в пространство <namespace> переменную <var>
#     get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
#
# Более формально, результатом работы get <namespace> <var> является
#
#     <namespace>, если в пространстве <namespace> была объявлена переменная <var>
#     get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
#     None, если не существует <parent>, т. е. <namespace> – это global
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.

spaces = {'global': {'parent': None, 'variables': set()}}  # nested dictionary with all spaces

# functions that asked in task

def create(namespace, parent):
    spaces[namespace] = {'parent': parent, 'variables': set()}


def add_arg(namespace, arg):
    spaces[namespace]['variables'].add(arg)


def get_space(namespace, arg):
    if namespace in spaces:
        if arg in spaces[namespace]['variables']:
            return namespace
        else:
            return get_space(spaces[namespace]['parent'], arg)
    else:
        return None

# input part

n = int(input())
for i in range(n):
    command, arg1, arg2 = input().split()
    if command == 'create':
        create(arg1, arg2)
    elif command == 'add':
        add_arg(arg1, arg2)
    elif command == 'get':
        print(get_space(arg1, arg2))