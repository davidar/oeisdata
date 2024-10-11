def A010060(n): return n.bit_count()&1 # _Chai Wah Wu_, Mar 01 2023
print([A010060(n) for n in range(30)])
