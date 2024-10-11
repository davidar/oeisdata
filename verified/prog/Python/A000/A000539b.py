def A000539(n): return n**2*(n**2*(n*(n+3<<1)+5)-1)//12 # _Chai Wah Wu_, Oct 03 2024
print([A000539(n) for n in range(30)])
