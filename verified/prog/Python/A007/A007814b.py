def A007814(n): return (~n & n-1).bit_length() # _Chai Wah Wu_, Jul 01 2022
print([A007814(n) for n in range(1,31)])
