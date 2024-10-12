def A003602(n): return (n>>(n&-n).bit_length())+1 # _Chai Wah Wu_, Jul 08 2022
print([A003602(n) for n in range(1,31)])
