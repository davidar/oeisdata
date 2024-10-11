def A001196(n): return 3*int(bin(n)[2:],4) # _Chai Wah Wu_, Aug 21 2023
print([A001196(n) for n in range(30)])
