def A004159(n):
    return sum(int(d) for d in str(n*n)) # _Chai Wah Wu_, Sep 03 2014
print([A004159(n) for n in range(30)])
