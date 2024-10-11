from math import comb
def A006013(n): return comb(3*n+1,n)//(n+1) # _Chai Wah Wu_, Jul 30 2022
print([A006013(n) for n in range(30)])
