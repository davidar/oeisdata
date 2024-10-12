def A023416(n): return n.bit_length()-n.bit_count() if n else 1 # _Chai Wah Wu_, Mar 13 2023
print([A023416(n) for n in range(30)])
