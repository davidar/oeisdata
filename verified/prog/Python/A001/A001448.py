from math import comb
def A001448(n): return comb(n<<2,n<<1) # _Chai Wah Wu_, Aug 10 2023
print([A001448(n) for n in range(30)])
