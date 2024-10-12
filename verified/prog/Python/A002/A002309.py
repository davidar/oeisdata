def A002309(n): return n*(n**2*(6*n**2-5<<3)+7)//15 # _Chai Wah Wu_, Oct 02 2024
print([A002309(n) for n in range(1,31)])
