n = int(input())
m = 0
for _ in range(n):
    r = int(input())
    if r % 5 == 0 and r > m:
        m = r
print(m)