n = int(input())
count, flag0 = 0, False
for _ in range(n):
    i = int(input())
    if i < 5:
        count += 1
    if i == 10:
        flag0 = True
print(count)
if flag0:
    print('YES')
else:
    print('NO')