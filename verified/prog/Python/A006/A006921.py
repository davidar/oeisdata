def A006921(n): return sum(int(not r & ~(n-r))*2**(n//2-r) for r in range(n//2+1)) # _Chai Wah Wu_, Jun 20 2022
print([A006921(n) for n in range(30)])
