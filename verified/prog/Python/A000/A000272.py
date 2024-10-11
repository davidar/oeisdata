def A000272(n): return 1 if n <= 1 else n**(n-2) # _Chai Wah Wu_, Feb 03 2022
print([A000272(n) for n in range(30)])
