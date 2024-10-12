from sympy import primepi
def A002808(n):
    m, k = n, primepi(n) + 1 + n
    while m != k:
        m, k = k, primepi(k) + 1 + n
    return m # _Chai Wah Wu_, Jul 15 2015, updated Apr 14 2016
print([A002808(n) for n in range(1,31)])
