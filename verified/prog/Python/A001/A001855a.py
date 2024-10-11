def A001855(n):
    s, i, z = 0, n-1, 1
    while 0 <= i: s += i; i -= z; z += z
    return s
print([A001855(n) for n in range(1, 59)]) # _Peter Luschny_, Nov 30 2017