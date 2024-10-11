def A004525(n): return ((n>>1)&-2)+bool(n&3) # _Chai Wah Wu_, Jan 27 2023
print([A004525(n) for n in range(30)])
