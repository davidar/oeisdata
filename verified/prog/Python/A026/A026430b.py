def A026430(n): return n+(n-1>>1)+(n-1&1|(n.bit_count()&1^1)) # _Chai Wah Wu_, Mar 01 2023
print([A026430(n) for n in range(30)])
