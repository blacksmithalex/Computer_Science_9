n = int(input())
min = 30000
for _ in range(n):
    a = int(input())
    if a % 10 == 4 and a < min:
        min = a
print(min)