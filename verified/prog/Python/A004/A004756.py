def A004756(n): return n+(3<<n.bit_length()-1) # _Chai Wah Wu_, Jul 13 2022
print([A004756(n) for n in range(1,31)])
