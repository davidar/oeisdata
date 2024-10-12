from sympy import npartitions
def A024786(n): return sum(npartitions(n-(k<<1)) for k in range(1,(n>>1)+1)) # _Chai Wah Wu_, Oct 25 2023
print([A024786(n) for n in range(1,31)])
