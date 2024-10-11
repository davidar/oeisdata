def A000537(n): return (n*(n+1)>>1)**2 # _Chai Wah Wu_, Oct 20 2023
print([A000537(n) for n in range(30)])
