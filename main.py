def to7(n):
    res = ''
    while n != 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]

print(to7(125))