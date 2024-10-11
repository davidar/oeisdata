def a():
    a, b, p = 0, 1, 1
    while True:
        yield a
        p, a, b = p + p, b, b + p * a
A015463 = a()
print([next(A015463) for _ in range(20)]) # _Peter Luschny_, Dec 05 2017