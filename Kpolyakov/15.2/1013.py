s, count = 0, 0
a = int(input())
while a != 0:
    if 100 <= a <= 999:
        s += a
        count += 1
    a = int(input())
if count == 0:
    print('NO')
else:
    print(s / count)

