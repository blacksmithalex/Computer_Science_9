n = int(input())
count, sum = 0, 0
while n != 0:
    if 99 < n < 1000:
        count += 1
        sum += n
    n = int(input())
if count != 0:
    print(sum / count)
else:
    print('NO')