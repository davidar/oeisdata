def A010888(n):
    return 1 + (n - 1) % 9 if n else 0 # _Chai Wah Wu_, Aug 23 2014, Apr 23 2023
print([A010888(n) for n in range(30)])
