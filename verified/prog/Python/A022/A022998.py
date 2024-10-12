def A022998(n): return n if n&1 else n<<1 # _Chai Wah Wu_, Mar 05 2024
print([A022998(n) for n in range(30)])
