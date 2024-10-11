def A000447(n): return n*((n**2<<2)-1)//3 # _Chai Wah Wu_, Feb 12 2023
print([A000447(n) for n in range(30)])
