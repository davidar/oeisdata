from math import isqrt
def A027434(n): return 1+isqrt((n<<2)-1) # _Chai Wah Wu_, Jul 27 2022
print([A027434(n) for n in range(1,31)])
