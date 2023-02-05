s, n = 0, 0
a = int(input())
while a != 0:
    if len(str(a)) == 2:
        s += a
        n += 1
    a = int(input())

if s == 0:
    print('NO')
else:
    print(s / n)

