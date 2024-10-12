def A027424(n): return len({i*j for i in range(1,n+1) for j in range(1,i+1)}) # _Chai Wah Wu_, Oct 13 2023
print([A027424(n) for n in range(1,31)])
