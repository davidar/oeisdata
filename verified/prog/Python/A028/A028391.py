from math import isqrt
def A028391(n): return n-isqrt(n) # _Chai Wah Wu_, Jul 28 2022
print([A028391(n) for n in range(30)])
