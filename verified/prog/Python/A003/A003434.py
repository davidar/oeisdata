from sympy import totient
def A003434(n):
    c, m = 0, n
    while m > 1:
        c += 1
        m = totient(m)
    return c # _Chai Wah Wu_, Nov 14 2021
print([A003434(n) for n in range(1,31)])
