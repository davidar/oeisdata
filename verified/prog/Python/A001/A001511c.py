def A001511(n): return (~n & n-1).bit_length()+1 # _Chai Wah Wu_, Jul 01 2022
print([A001511(n) for n in range(1,31)])
