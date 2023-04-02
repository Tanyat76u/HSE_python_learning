# i = int(input())
# while i <= 100:
#     print(i, end= ' ')
#     i = i + 2
# print('цикл завершен')

now = int(input())
Max = now
while now != 0:
    now = int(input())
    if now > Max:
        Max = now
print(Max)
