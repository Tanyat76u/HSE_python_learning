# Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи
# (вторую справа цифру или 0, если число меньше 10).
#
# Предполагается решение этой задачи без использования строковых методов. Пожалуйста, пользуйтесь арифметикой.
#
a = int(input())
if a < 10:
    print(0)
else:
    print(a // 10 % 10)
