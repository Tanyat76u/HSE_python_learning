# Дано трехзначное число. Найдите сумму его цифр.

a = int(input())
if 100 <= a <= 999:
    print(a // 100 + a // 10 % 10 + a % 10)