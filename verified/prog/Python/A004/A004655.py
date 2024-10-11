def A004655(n): return 10**(n>>2)<<(n&3) # _Chai Wah Wu_, Jan 27 2023
print([A004655(n) for n in range(30)])
