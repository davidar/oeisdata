def A003417(n): return 2 if n == 0 else 1 if n % 3 != 2 else (n+1)//3<<1 # _Chai Wah Wu_, Jul 27 2022
print([A003417(n) for n in range(30)])
