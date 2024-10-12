from sympy import prime, n_order
def A002371(n): return 0 if n == 1 or n == 3 else n_order(10,prime(n)) # _Chai Wah Wu_, Feb 07 2022
print([A002371(n) for n in range(1,31)])
