def A003278(n):
    return int(format(n-1,'b'),3)+1 # _Chai Wah Wu_, Jan 04 2015
print([A003278(n) for n in range(1,31)])
