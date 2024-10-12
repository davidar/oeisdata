def A001651(n): return (n<<1)-(n>>1)-1 # _Chai Wah Wu_, Mar 05 2024
print([A001651(n) for n in range(1,31)])
