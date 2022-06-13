N = int(input())
M, flag0 = 0, False
for _ in range(N):
    r = int(input())
    if r > M:
        M = r
    if r == 0:
        flag0 = True
print(M)
if flag0:
    print('YES')
else:
    print('NO')