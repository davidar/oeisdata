def a(n):
    a, b = 1, 0
    while n > 0:
        if n & 1:
            b += a
        else:
            a += b
        n >>= 1
    return b
# _Reza K Ghazi_, Dec 29 2021
print([a(n) for n in range(30)])
