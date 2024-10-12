def A002804(n): return (1<<n)+(3**n>>n)-2 # _Chai Wah Wu_, Jun 25 2024
print([A002804(n) for n in range(1,31)])
