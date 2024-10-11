def A001787(n): return n*(1<<n-1) if n else 0 # _Chai Wah Wu_, Nov 14 2022
print([A001787(n) for n in range(30)])
