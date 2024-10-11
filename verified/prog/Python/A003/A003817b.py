def A003817(n): return (1<<n.bit_length())-1 # _Chai Wah Wu_, Jul 17 2024
print([A003817(n) for n in range(30)])
