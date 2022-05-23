n = int(input())
count = 0
for _ in range(n):
    r = int(input())
    if r % 4 == 0 and r % 7 != 0:
        count += 1
print(count)