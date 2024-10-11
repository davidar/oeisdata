def A002487(n): return sum(int(not (n-k-1) & ~k) for k in range(n)) # _Chai Wah Wu_, Jun 19 2022
print([A002487(n) for n in range(30)])
