from sympy import primefactors
def A010055(n): return int(len(primefactors(n)) <= 1) # _Chai Wah Wu_, Mar 31 2023
print([A010055(n) for n in range(1,31)])
