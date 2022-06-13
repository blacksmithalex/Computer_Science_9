n = int(input())
count = 0
sum = 0
while n != 0:
    if n % 8 == 0:
        count += 1
        sum += n
    n = int(input())
if count != 0:
    print(round(sum / count, 1))
else:
    print('NO')