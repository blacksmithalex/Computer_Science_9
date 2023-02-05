n = int(input())
count = 0
for _ in range(n):
    a = int(input())
    if a % 3 == 0 and a % 10 == 2:
        count += 1
print(count)


