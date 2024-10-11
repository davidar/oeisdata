from math import comb
def A000846(n): return comb(3*n,n)-comb(n<<1,n) # _Chai Wah Wu_, Sep 07 2022
print([A000846(n) for n in range(30)])
