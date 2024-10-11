def mot():
    a, b, n = 0, 1, 1
    while True:
        yield b//n
        n += 1
        a, b = b, (3*(n-1)*n*a+(2*n-1)*n*b)//((n+1)*(n-1))
A001006 = mot()
print([next(A001006) for n in range(30)]) # _Peter Luschny_, May 16 2016