from sympy import lucas
def A001350(n): return lucas(n)-((n&1^1)<<1) # _Chai Wah Wu_, Sep 23 2023
print([A001350(n) for n in range(30)])
