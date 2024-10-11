def A009545(n): return ((0, 1, 2, 2)[n&3]<<((n>>1)&-2))*(-1 if n&4 else 1) # _Chai Wah Wu_, Feb 16 2024
print([A009545(n) for n in range(30)])
