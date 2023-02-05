n = int(input())
count = 0
flag = False
for _ in range(n):
    a = int(input())
    if a < 5:
        count += 1
    if a == 10:
        flag = True
print(count)
if flag:
    print('YES')
else:
    print('NO')

