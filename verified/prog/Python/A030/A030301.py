def A030301(n): return n.bit_length()&1^1 # _Chai Wah Wu_, Jan 30 2023
print([A030301(n) for n in range(1,31)])
