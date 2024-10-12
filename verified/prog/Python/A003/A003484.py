def A003484(n): return (((m:=(~n&n-1).bit_length())&-4)<<1)+(1<<(m&3)) # _Chai Wah Wu_, Jul 09 2022
print([A003484(n) for n in range(1,31)])
