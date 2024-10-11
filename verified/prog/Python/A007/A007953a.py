def A007953(n):
    return sum(int(d) for d in str(n)) # _Chai Wah Wu_, Sep 03 2014
print([A007953(n) for n in range(30)])
