def A007310(n): return (n+(n>>1)<<1)-1 # _Chai Wah Wu_, Oct 10 2023
print([A007310(n) for n in range(1,31)])
