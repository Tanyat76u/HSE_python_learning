# Даны три целых числа. Найдите наибольшее из них
# (программа должна вывести ровно одно целое число).
#
# Какое наименьшее число операторов сравнения (>, <, >=, <=)
# необходимо для решения этой задачи?

a = int(input())
b = int(input())
c = int(input())

if a < b and c < b:
    print(b)
elif a < c > b:
    print(c)
elif c < a > b:
    print(a)
elif a == c > b:
    print(a)
elif b == c > a:
    print(b)
elif a == b > c:
    print(b)

