def A000788(n): return sum(i.bit_count() for i in range(1,n+1)) # _Chai Wah Wu_, Mar 01 2023
print([A000788(n) for n in range(30)])
