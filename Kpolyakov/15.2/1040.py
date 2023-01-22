count = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 4 and a % 6 == 0:
        count += 1
print(count)