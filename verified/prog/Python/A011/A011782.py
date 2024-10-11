def A011782(n): return 1 if n == 0 else 2**(n-1) # _Chai Wah Wu_, May 11 2022
print([A011782(n) for n in range(30)])
