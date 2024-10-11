def A003314(n):
    s, i, z = n-1, n-1, 1
    while 0 <= i: s += i; i -= z; z += z
    return s
print([A003314(n) for n in range(1, 58)]) # _Peter Luschny_, Nov 30 2017