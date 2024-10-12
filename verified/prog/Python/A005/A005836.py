def A005836(n):
    return int(format(n-1,'b'),3) # _Chai Wah Wu_, Jan 04 2015
print([A005836(n) for n in range(1,31)])
