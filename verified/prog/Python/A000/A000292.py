# Compare A000217.
def A000292():
    x, y, z = 1, 1, 1
    yield 0
    while True:
        yield x
        x, y, z = x + y + z + 1, y + z + 1, z + 1
a = A000292(); print([next(a) for i in range(45)]) # _Peter Luschny_, Aug 03 2019