a = int(input())
max = 0
for i in range(a):
    a = int(input())
    if a % 10 == 3 and a > max:
        max = a
print(max)