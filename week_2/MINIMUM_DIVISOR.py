
a = int(input())
b = 2
i = a % b

while i != 0:
    b = b + 1
    i = a % b
print(b)
