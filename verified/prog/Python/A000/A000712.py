from sympy import npartitions
def A000712(n): return (sum(npartitions(k)*npartitions(n-k) for k in range(n+1>>1))<<1) + (0 if n&1 else npartitions(n>>1)**2) # _Chai Wah Wu_, Sep 25 2023
print([A000712(n) for n in range(30)])
