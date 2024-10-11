from math import comb
def A001405(n): return comb(n,n//2) # _Chai Wah Wu_, Jun 07 2022
print([A001405(n) for n in range(30)])
