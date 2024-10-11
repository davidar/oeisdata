from math import comb
def A004381(n): return comb(n<<3,n) # _Chai Wah Wu_, Aug 01 2023
print([A004381(n) for n in range(30)])
