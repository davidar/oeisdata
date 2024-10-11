# based on _Vladimir Kruchinin_'s formula
def A000478():
    a = 15; n = 7; z = 4; s = 15;
    while True:
        yield a
        z = 2*z; s += n*(z-2) + 3; a = 3*a + s; n += 1
a = A000478(); print([next(a) for _ in range(6, 32)]) # _Peter Luschny_, Oct 04 2018