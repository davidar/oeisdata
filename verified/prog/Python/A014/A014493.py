def A014493(n): return ((n<<1)-1)*(n-(n&1^1)) # _Chai Wah Wu_, Feb 12 2023
print([A014493(n) for n in range(1,31)])
