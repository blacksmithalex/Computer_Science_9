s, count = 0, 0
a = int(input())
while a != 0:
    if a % 8 == 0:
        s += a
        count += 1
    a = int(input())

if count == 0:
    print('NO')
else:
    print(round(s / count, 1))

