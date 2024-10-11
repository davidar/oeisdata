def A010059(n): return n.bit_count()&1^1 # _Chai Wah Wu_, Mar 01 2023
print([A010059(n) for n in range(30)])
