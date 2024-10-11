def A020986(n): return sum(-1 if (m&(m>>1)).bit_count()&1 else 1 for m in range(n+1)) # _Chai Wah Wu_, Feb 11 2023
print([A020986(n) for n in range(30)])
