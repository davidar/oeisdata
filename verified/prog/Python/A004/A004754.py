def A004754(n): return n+(1<<n.bit_length()-1) # _Chai Wah Wu_, Jul 13 2022
print([A004754(n) for n in range(1,31)])
