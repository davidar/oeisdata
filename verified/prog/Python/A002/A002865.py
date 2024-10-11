from sympy import npartitions
def A002865(n): return npartitions(n)-npartitions(n-1) if n else 1 # _Chai Wah Wu_, Mar 30 2023
print([A002865(n) for n in range(30)])
