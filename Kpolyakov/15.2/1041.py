m3 = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 3 and a > m3:
        m3 = a
print(m3)