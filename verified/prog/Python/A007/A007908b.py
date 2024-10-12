from functools import reduce
def A007908(n): return reduce(lambda i,j:i*10**len(str(j))+j,range(1,n+1)) # _Chai Wah Wu_, Feb 27 2023
print([A007908(n) for n in range(1,31)])
