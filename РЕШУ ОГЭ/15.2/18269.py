r = int(input())
s8, count8 = 0, 0
while r != 0:
    if r % 8 == 0:
        s8 += r
        count8 += 1
    r = int(input())

if count8 != 0:
    print(round(s8 / count8, 1))
else:
    print('NO')