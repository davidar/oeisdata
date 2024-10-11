def A006943(n): return sum((bool(~n&n-k)^1)*10**k for k in range(n+1)) # _Chai Wah Wu_, May 03 2023
print([A006943(n) for n in range(30)])
