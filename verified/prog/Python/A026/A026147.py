def A026147(n): return 1+((m:=n-1).bit_count()&1)+(m<<1) # _Chai Wah Wu_, Mar 03 2023
print([A026147(n) for n in range(1,31)])
