"""Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков."""

a = int(input())
b = int(input())
n = int(input())
"""if b > 60:
    a + 1"""
print(a * n + (b * n // 100), b * n % 100)
# 10 0     2 50 4     10 15 2   20 30
