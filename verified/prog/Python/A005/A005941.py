from sympy import primepi, factorint
def A005941(n): return sum((1<<primepi(p)-1)<<i for i, p in enumerate(factorint(n, multiple=True)))+1 # _Chai Wah Wu_, Mar 11 2023
print([A005941(n) for n in range(1,31)])
