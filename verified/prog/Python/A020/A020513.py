from sympy import primefactors
def A020513(n): return (-1,-2,0)[n] if n<3 else (f[0] if n&1^1 and len(f:=primefactors(n>>1))==1 else 1) # _Chai Wah Wu_, Aug 26 2024
print([A020513(n) for n in range(30)])
