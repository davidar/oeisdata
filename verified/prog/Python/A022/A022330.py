def A022330(n): return sum((3**i).bit_length() for i in range(n+1)) # _Chai Wah Wu_, Sep 16 2024
print([A022330(n) for n in range(30)])
