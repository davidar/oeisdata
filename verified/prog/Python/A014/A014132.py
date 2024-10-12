from math import isqrt
def A014132(n): return n+(isqrt((n<<3)-7)+1>>1) # _Chai Wah Wu_, Jun 17 2024
print([A014132(n) for n in range(1,31)])
