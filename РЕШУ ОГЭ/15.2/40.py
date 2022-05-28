n = int(input())
sum = 0
for _ in range(n):
    r = int(input())
    if r % 6 == 0:
        sum += r
print(sum)