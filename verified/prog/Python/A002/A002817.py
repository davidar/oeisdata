def A002817(n): return (m:=n*(n+1))*(m+2)>>3 # _Chai Wah Wu_, Aug 30 2024
print([A002817(n) for n in range(30)])
