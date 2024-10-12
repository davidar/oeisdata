def A000523(n):
    return len(bin(n))-3 # _Chai Wah Wu_, Jul 09 2020
print([A000523(n) for n in range(1,31)])
