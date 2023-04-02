a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
hours = (d - a) * 3600
minutes = (e - b) * 60
seconds = (f - c) + hours + minutes
print(seconds)
hour1 = int(input())
min1 = int(input())
sec1 = int(input())
hour2 = int(input())
min2 = int(input())
sec2 = int(input())
print(((((hour2 * 60 + 2) * 60)-((hour1 * 60 + 1) * 60)) % 24) * 3, (((((hour2 * 60 + 2) * 60)-((hour1 * 60 + 1) * 60)) % 24) * 3) // 3 * 5 + 1, sep='')