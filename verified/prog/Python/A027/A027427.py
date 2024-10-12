def A027427(n): return 1+len({i*j for i in range(1,n+1) for j in range(1,i)}) if n else 0 # _Chai Wah Wu_, Oct 13 2023
print([A027427(n) for n in range(30)])
