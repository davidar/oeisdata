from sympy import primefactors
def A005087(n): return len(primefactors(n))+(n&1)-1 # _Chai Wah Wu_, Jul 07 2022
print([A005087(n) for n in range(1,31)])
