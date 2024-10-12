def A010846(n): return sum((m:=n**k)//k-(m-1)//k for k in range(1,n+1)) # _Chai Wah Wu_, Aug 15 2024
print([A010846(n) for n in range(1,31)])
