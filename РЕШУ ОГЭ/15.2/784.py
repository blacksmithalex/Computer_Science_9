a = int(input())
sum = 0
while a != 0:
    if a % 6 == 0 and a % 10 == 4:
        sum += a
    a = int(input())
print(sum)