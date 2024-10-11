def A004086(n):
    return int(str(n)[::-1]) # _Chai Wah Wu_, Aug 30 2014
print([A004086(n) for n in range(30)])
