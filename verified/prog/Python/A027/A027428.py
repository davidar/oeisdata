def A027428(n): return len({i*j for i in range(1,n+1) for j in range(1,i)}) # _Chai Wah Wu_, Oct 13 2023
print([A027428(n) for n in range(1,31)])
