def A008805(n): return (m:=(n>>1)+1)*(m+1)>>1 # _Chai Wah Wu_, Oct 20 2023
print([A008805(n) for n in range(30)])
