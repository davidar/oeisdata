def A020985(n): return -1 if (n&(n>>1)).bit_count()&1 else 1 # _Chai Wah Wu_, Feb 11 2023
print([A020985(n) for n in range(30)])
