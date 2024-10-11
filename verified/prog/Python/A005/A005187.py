def A005187(n): return 2*n-bin(n).count('1') # _Chai Wah Wu_, Jun 03 2021
print([A005187(n) for n in range(30)])
