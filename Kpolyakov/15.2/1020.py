n = int(input())
m = 0
flag = False
for _ in range(n):
    a = int(input())
    if a > m:
        m = a
    if a == 0:
        flag = True
print(m)
if flag:
    print('YES')
else:
    print('NO')

