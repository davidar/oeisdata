def A027430(n): return len({i*j*k for i in range(1,n+1) for j in range(1,i) for k in range(1,j)}) # _Chai Wah Wu_, Oct 16 2023
print([A027430(n) for n in range(1,31)])
