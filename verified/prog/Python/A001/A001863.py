from math import comb
def A001863(n): return 0 if n<2 else ((sum(comb(n,k)*(n-k)**(n-k)*k**k for k in range(1,(n+1>>1)))<<1) + (0 if n&1 else comb(n,m:=n>>1)*m**n))//n//(n-1) # _Chai Wah Wu_, Apr 25-26 2023
print([A001863(n) for n in range(1,31)])
