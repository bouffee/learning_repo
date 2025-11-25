# Напишите программу, которая считывает текст из файла 
# (в файле может быть больше одной строки) и выводит самое частое слово 
# в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов 
# несколько, вывести лексикографически первое (можно использовать оператор < 
# для строк).

# Слова, написанные в разных регистрах, считаются одинаковыми.



words = {} #словарь всех слов в файле

with open ("dataset_3363_3.txt") as inf:
    for line in inf:
        line = line.lower()
        for word in line.split(): #запись слов в словарь
            if word not in words:
                words.update({word: 1})
            else:
                words[word] += 1

max_amount = 1

for key, value in words.items(): #поиск слова, которое в словаре по количеству максимальное
    curr_amount = words[key]
    if curr_amount > max_amount:
        max_amount = curr_amount
        max_amount_word = key

with open("output.txt", 'w') as outf:
    popular = (max_amount_word + ' ' + str(max_amount))
    outf.write(popular)