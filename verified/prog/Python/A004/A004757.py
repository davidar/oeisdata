def A004757(n): return n+(2<<n.bit_length()) # _Chai Wah Wu_, Jul 13 2022
print([A004757(n) for n in range(1,31)])
