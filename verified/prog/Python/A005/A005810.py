from math import comb
def A005810(n): return comb(n<<2,n) # _Chai Wah Wu_, Aug 01 2023
print([A005810(n) for n in range(30)])
