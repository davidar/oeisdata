def A002662(n): return (1<<n)-1-(n*(n+1)>>1) # _Chai Wah Wu_, Aug 29 2023
print([A002662(n) for n in range(30)])
