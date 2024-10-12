def A001855(n): return n*(m:=(n-1).bit_length())-(1<<m)+1 # _Chai Wah Wu_, Mar 29 2023
print([A001855(n) for n in range(1,31)])
