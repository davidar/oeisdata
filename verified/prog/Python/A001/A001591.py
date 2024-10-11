def pentanacci():
    a, b, c, d, e = 0, 0, 0, 0, 1
    while True:
        yield a
        a, b, c, d, e = b, c, d, e, a + b + c + d + e
f = pentanacci()
print([next(f) for _ in range(100)]) # _Reza K Ghazi_ Apr 09 2021