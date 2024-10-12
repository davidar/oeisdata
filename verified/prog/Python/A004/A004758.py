def A004758(n): return n+(5<<n.bit_length()-1) # _Chai Wah Wu_, Jul 13 2022
print([A004758(n) for n in range(1,31)])
