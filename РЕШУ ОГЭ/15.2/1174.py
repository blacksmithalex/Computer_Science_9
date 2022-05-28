r = int(input())
count = 0
while r != 0:
    if 100 <= r <= 999 and r % 4 == 0:
        count += 1
    r = int(input())
print(count)