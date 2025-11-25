# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days
# Sample Input 1:
# 2016 4 20
# 14
#
# Sample Output 1:
# 2016 5 4

import datetime
year, month, day = map(int, input().split())
date = datetime.datetime(year=year, month=month, day=day)
num_days = int(input())
res = date + datetime.timedelta(days=num_days)
print(res.strftime('%Y %m %d').replace(' 0', ' '))