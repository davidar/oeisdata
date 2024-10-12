from sympy import factorint
def A008836(n): return -1 if sum(factorint(n).values()) % 2 else 1 # _Chai Wah Wu_, May 24 2022
print([A008836(n) for n in range(1,31)])
