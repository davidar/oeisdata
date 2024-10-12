def A004759(n): return n+(3<<n.bit_length()) # _Chai Wah Wu_, Jul 13 2022
print([A004759(n) for n in range(1,31)])
