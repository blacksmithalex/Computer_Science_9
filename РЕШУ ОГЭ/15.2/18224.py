n = int(input())
sum = 0
for _ in range(n):
    i = int(input())
    if i % 10 == 8:
        sum += i
print(sum)