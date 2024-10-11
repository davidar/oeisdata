def A006125(n): return 1<<(n*(n-1)>>1) # _Chai Wah Wu_, Nov 09 2023
print([A006125(n) for n in range(30)])
