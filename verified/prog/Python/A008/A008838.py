def A008838(n): return (m:=n>>3)*(m+bool(n&7)) # _Chai Wah Wu_, Jan 19 2023
print([A008838(n) for n in range(30)])
