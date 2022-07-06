a = int(input())
count = 0
while a != 0:
    a = int(input())
    if a % 2 == 0 and a % 5 == 0:
        count += 1
print(count)