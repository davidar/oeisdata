def A006520(n): return sum(i&-i for i in range(1,n+1)) # _Chai Wah Wu_, Jul 14 2022
print([A006520(n) for n in range(1,31)])
