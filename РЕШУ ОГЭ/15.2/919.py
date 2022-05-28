r = int(input())
sum = 0
while r != 0:
    if r % 3 == 0 and r % 10 == 9:
        sum += r
    r = int(input())
print(sum)