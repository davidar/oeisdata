from sympy import primefactors
def A005091(n): return sum(1 for p in primefactors(n) if p&3==3) # _Chai Wah Wu_, Jul 07 2024
print([A005091(n) for n in range(1,31)])
