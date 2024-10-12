def A003314(n): return n*(1+(m:=(n-1).bit_length()))-(1<<m) # _Chai Wah Wu_, Mar 29 2023
print([A003314(n) for n in range(1,31)])
