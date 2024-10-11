def a(n):
    k, pow3, m = 0, 1, 11
    while n + m > 0:
        n, rn = divmod(n, 3)
        m, rm = divmod(m, 3)
        k, pow3 = k + pow3*((rn+rm)%3), pow3*3
    return k
print([a(n) for n in range(58)]) # _Michael S. Branicky_, Nov 09 2021