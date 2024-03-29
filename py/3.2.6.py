# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.

# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.

# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) 
# в формате "слово количество".
# Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.

a = input().lower().split()
b = {}
for elem in a:
    if elem in b:
        b[elem] += 1
    else:
        b.update({elem: 1})
for key, value in b.items():
    print(key, value, end = '\n')