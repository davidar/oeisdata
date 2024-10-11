def A010883(n): return 1 + (n & 3) # _Chai Wah Wu_, May 25 2022
print([A010883(n) for n in range(30)])
