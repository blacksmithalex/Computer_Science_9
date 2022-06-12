N = int(input())
s, count = 0, 0
flag60 = False

for _ in range(N):
    v = int(input())
    if v >= 60:
        flag60 = True
    s += v
    count += 1

print(round(s / count, 1))
if flag60:
    print('YES')
else:
    print('NO')
