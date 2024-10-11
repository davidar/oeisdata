def A014848(n): return n**2-(n>>1) # _Chai Wah Wu_, Jan 18 2023
print([A014848(n) for n in range(30)])
