'''
s = 0
a = int(input())
while a != 0:
    if a // 1000 == 0 and a // 100 != 0 and a % 4 == 0:
        s += a
    a = int(input())
print(s)
'''
s = 0
a = int(input())
while a != 0:
    if len(str(a)) == 3 and a % 4 == 0:
        s += a
    a = int(input())
print(s)

