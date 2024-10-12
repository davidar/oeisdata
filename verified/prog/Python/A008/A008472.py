from sympy import primefactors
def A008472(n): return sum(primefactors(n)) # _Chai Wah Wu_, Feb 03 2022
print([A008472(n) for n in range(1,31)])
