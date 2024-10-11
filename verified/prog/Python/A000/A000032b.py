from sympy import lucas
def A000032(n): return lucas(n) # _Chai Wah Wu_, Sep 23 2023
print([A000032(n) for n in range(30)])
