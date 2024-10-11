def A006003(n): return n*(n**2+1)>>1 # _Chai Wah Wu_, Mar 25 2024
print([A006003(n) for n in range(30)])
