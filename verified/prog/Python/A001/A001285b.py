def A001285(n): return 2 if n.bit_count()&1 else 1 # _Chai Wah Wu_, Mar 01 2023
print([A001285(n) for n in range(30)])
