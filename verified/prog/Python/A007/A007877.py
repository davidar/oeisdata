def A007877(n): return (0,1,2,1)[n&3] # _Chai Wah Wu_, Jan 26 2023
print([A007877(n) for n in range(30)])
