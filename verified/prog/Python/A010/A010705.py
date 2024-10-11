def A010705(n): return 3|((n&1)<<2) # _Chai Wah Wu_, Aug 12 2023
print([A010705(n) for n in range(30)])
