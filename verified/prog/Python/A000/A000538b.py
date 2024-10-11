def A000538(n): return n*(n**2*(n*(6*n+15)+10)-1)//30 # _Chai Wah Wu_, Oct 03 2024
print([A000538(n) for n in range(30)])
