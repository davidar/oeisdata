def A004647(n): return int(oct(2**n)[2:]) # _Chai Wah Wu_, May 23 2022
print([A004647(n) for n in range(30)])
