def A028310(n): return n|bool(n)^1 # _Chai Wah Wu_, Jul 13 2023
print([A028310(n) for n in range(30)])
