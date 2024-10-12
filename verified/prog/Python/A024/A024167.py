def A():
    a, b, n = 1, 1, 2
    yield(a)
    while True:
        yield(a)
        b, a = a, a + b * n * n
        n += 1
a = A(); print([next(a) for _ in range(20)]) # _Peter Luschny_, May 19 2020