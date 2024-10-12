from sympy import primepi
def A014076(n):
    if n == 1: return 1
    m, k = n-1, primepi(n) + n - 1 + (n>>1)
    while m != k:
        m, k = k, primepi(k) + n - 1 + (k>>1)
    return m # _Chai Wah Wu_, Jul 31 2024
print([A014076(n) for n in range(1,31)])
