def A000069(n): return ((m:=n-1)<<1)+(m.bit_count()&1^1) # _Chai Wah Wu_, Mar 03 2023
print([A000069(n) for n in range(1,31)])
