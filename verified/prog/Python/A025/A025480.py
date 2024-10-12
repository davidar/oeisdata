def A025480(n): return n>>((~(n+1)&n).bit_length()+1) # _Chai Wah Wu_, Jul 13 2022
print([A025480(n) for n in range(30)])
