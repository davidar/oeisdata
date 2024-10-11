def A003188(n): return n^ n>>1 # _Chai Wah Wu_, Jun 29 2022
print([A003188(n) for n in range(30)])
