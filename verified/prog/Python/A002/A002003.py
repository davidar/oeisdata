from math import comb
def A002003(n): return sum(comb(n,k)**2*k<<k-1 for k in range(1,n+1))//n<<1 if n else 0 # _Chai Wah Wu_, Mar 22 2023
print([A002003(n) for n in range(30)])
