from math import comb
def A001764(n): return comb(3*n,n)//(2*n+1) # _Chai Wah Wu_, Nov 10 2022
print([A001764(n) for n in range(30)])
