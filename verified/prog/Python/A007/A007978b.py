def A007978(n): return next(filter(lambda d:n%d,range(2,n))) if n>2 else n+1 # _Chai Wah Wu_, Feb 22 2023
print([A007978(n) for n in range(1,31)])
