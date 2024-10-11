def A008217(n): return (n>>2)*(n+1>>2) # _Chai Wah Wu_, Feb 02 2023
print([A008217(n) for n in range(30)])
