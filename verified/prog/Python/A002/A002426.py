from math import comb
def A002426(n): return sum(comb(n,k)*comb(k,n-k) for k in range(n+1)) # _Chai Wah Wu_, Nov 15 2022
print([A002426(n) for n in range(30)])
