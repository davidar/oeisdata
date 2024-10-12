def A001969(n): return ((m:=n-1).bit_count()&1)+(m<<1) # _Chai Wah Wu_, Mar 03 2023
print([A001969(n) for n in range(1,31)])
