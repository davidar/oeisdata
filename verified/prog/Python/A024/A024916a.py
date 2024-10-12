def A024916(n): return sum(k*(n//k) for k in range(1,n+1)) # _Chai Wah Wu_, Dec 17 2021
print([A024916(n) for n in range(1,31)])
