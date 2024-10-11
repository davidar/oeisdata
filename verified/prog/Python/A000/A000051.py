def A000051(n): return (1<<n)|1 if n else 2 # _Chai Wah Wu_, Dec 21 2022
print([A000051(n) for n in range(30)])
