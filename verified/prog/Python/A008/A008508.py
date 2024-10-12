from sympy import primepi
def A008508(n):
    if n == 1: return 3
    m, k = n, (r:=primepi(n)) + n + (n>>1)
    while m != k:
        m, k = k, (r:=primepi(k)) + n + (k>>1)
    return r-1 # _Chai Wah Wu_, Aug 01 2024
print([A008508(n) for n in range(1,31)])
