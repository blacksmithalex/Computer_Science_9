n = int(input())
count = 0
for _ in range(n):
    a = int(input())
    if a % 4 == 0 and a % 7 != 0:
        count += 1
print(count)