from math import comb
def A014068(n): return comb(comb(n+1,2),n) # _Chai Wah Wu_, Jul 14 2024
print([A014068(n) for n in range(30)])
