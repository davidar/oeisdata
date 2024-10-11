def A000695(n): return int(bin(n)[2:],4) # _Chai Wah Wu_, Aug 21 2023
print([A000695(n) for n in range(30)])
