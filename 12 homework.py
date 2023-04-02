A = int(input())
B = int(input())
N = int(input())
cost1 = ((A * 100 + B) * N) % 100
cost2 = ((A * 100 + B) * N) // 100
print(cost2, cost1)
