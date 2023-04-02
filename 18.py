n = int(input())
hour = n // 60 // 60 % 24
min1 = n // 60 % 60 // 10
min2 = n // 60 % 60 % 10
sec1 = n % 60 // 10
sec2 = n % 60 % 10
print(hour, ':', min1, min2, ':', sec1, sec2, sep='')
