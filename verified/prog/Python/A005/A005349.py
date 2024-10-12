A005349 = [n for n in range(1,10**6) if not n % sum([int(d) for d in str(n)])] # _Chai Wah Wu_, Aug 22 2014
print(A005349)
