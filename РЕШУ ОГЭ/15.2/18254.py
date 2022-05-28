a = int(input())
s, count = 0, 0
while a != 0:
    if 10 <= a < 100:
        s, count = s + a, count + 1
    a = int(input())
if s != 0:
    print(round(s / count, 1))
else:
    print('NO')

