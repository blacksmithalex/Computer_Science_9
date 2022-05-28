n = int(input())
sum = 0
for _ in range(n):
    r = int(input())
    if r % 10 == 3:
        sum += r
print(sum)