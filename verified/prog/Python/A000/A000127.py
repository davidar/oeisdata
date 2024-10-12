def A000127(n): return n*(n*(n*(n - 6) + 23) - 18)//24 + 1 # _Chai Wah Wu_, Sep 18 2021
print([A000127(n) for n in range(1,31)])
