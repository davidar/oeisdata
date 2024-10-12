def A027425(n): return len({i*j*k for i in range(1,n+1) for j in range(1,i+1) for k in range(1,j+1)}) # _Chai Wah Wu_, Oct 16 2023
print([A027425(n) for n in range(1,31)])
