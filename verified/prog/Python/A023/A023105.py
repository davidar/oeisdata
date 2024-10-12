def A023105(n): return ((1<<n-1)+5)//3 if n else 1 # _Chai Wah Wu_, Aug 22 2023
print([A023105(n) for n in range(30)])
