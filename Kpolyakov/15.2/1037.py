a = int(input())
count = 0
while a != 0:
    if a % 5 == 0 or a % 9 == 0:
        count += 1
    a = int(input())
print(count)
