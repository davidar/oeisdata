from math import isqrt
def A027709(n): return 1+isqrt((n<<2)-1)<<1 if n else 0 # _Chai Wah Wu_, Jul 28 2022
print([A027709(n) for n in range(30)])
