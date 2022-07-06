a = int(input())
count = 0
for i in range(a):
    a = int(input())
    if a % 10 == 2 and a % 3 == 0:
        count += 1
print(count)