def A030300(n): return n.bit_length()&1 # _Chai Wah Wu_, Jan 30 2023
print([A030300(n) for n in range(1,31)])
