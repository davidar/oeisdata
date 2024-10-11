def A014550(n): return int(bin(n^n>>1)[2:]) # _Chai Wah Wu_, May 31 2024
print([A014550(n) for n in range(30)])
