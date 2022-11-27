# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Класс A является предком класса B, если
#     A = B;
#     A - прямой предок B
#     существует такой класс C, что C - прямой предок B и A - предок C
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
#
# Формат входных данных:
#
# В первой строке входных данных содержится целое число n - число классов.
# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс.
# Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.
# В следующей строке содержится число q - количество запросов.
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
#
# Формат выходных данных:
#
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.


all_classes = dict()  # dictionary for all classes

# first input with declaring classes and their parents/children

n1 = int(input())
for i in range(n1):
   child, *parent = input().replace(':', ' ').split()
   if child not in all_classes:
      all_classes[child] = parent
   else:
      for item in parent:
         all_classes[child].append(item)

# transformation of the dictionary. Adding to child all his parents

for key_1, value_1 in all_classes.items():
   for key_2, value_2 in all_classes.items():
      if key_1 in value_2:
         for item in value_1:
            value_2.append(item)

# second input part with checking is first class is parent of second class

n2 = int(input())
for i in range(n2):
   check_child, check_parent = input().split()
   if check_child not in all_classes.keys():  # check if actually child was declared before
      print('No')
      continue
   elif check_parent == check_child:  # if parent and child are the same then they are parent and child of each other
      print('Yes')
   elif check_child in all_classes[check_parent]:  # check if child is in list of parent class' children
      print('Yes')
   else:
      print('No')