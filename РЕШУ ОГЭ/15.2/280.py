N = int(input())
m4 = 1000
for _ in range(N):
    r = int(input())
    if r % 10 == 4 and r < m4:
        m4 = r
print(m4)