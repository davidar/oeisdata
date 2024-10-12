def A007413(n): return 2-(n.bit_count()&1)+((n-1).bit_count()&1) # _Chai Wah Wu_, Mar 03 2023
print([A007413(n) for n in range(1,31)])
