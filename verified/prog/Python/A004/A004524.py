def A004524(n): return (n>>2)+(n+1>>2) # _Chai Wah Wu_, Jul 29 2022
print([A004524(n) for n in range(30)])
