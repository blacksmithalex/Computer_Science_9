a = int(input())
b = int(input())
count = 0
for n in range(a, b + 1):
    if n % 2 == 0:
        count += 1
print(count)