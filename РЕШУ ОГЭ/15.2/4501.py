N = int(input())
s, count, above = 0, 0, 0
for _ in range(N):
    t = int(input())
    s += t
    count += 1
    if t >= 0:
        above += 1

print(s / count)
if above >= 5:
    print('YES')
else:
    print('NO')