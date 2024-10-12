def A029931(n): return sum(i if j == '1' else 0 for i, j in enumerate(bin(n)[:1:-1],1)) # _Chai Wah Wu_, Dec 20 2022
print([A029931(n) for n in range(30)])
