n = int(input())
m = int(input())
d = m // n + 1 - 0 ** (m % n)   # чужой вариант верный
print(d)

#мой вариант неверно
n = int(input())
m = int(input())
print(m // (n // 24) // 24 + 1)