r = int(input())
count = 0
sum = 0
while r != 0:
    count += 1
    if r % 2 == 0:
        sum += r
    r = int(input())
print(count, sum)