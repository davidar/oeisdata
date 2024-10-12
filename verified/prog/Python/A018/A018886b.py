def A018886(n): return (3**n&-(1<<n))-1 # _Chai Wah Wu_, Jun 25 2024
print([A018886(n) for n in range(1,31)])
