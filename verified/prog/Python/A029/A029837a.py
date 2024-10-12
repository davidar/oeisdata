def A029837(n):
    s = bin(n)[2:]
    return len(s) - (1 if s.count('1') == 1 else 0) # _Chai Wah Wu_, Jul 09 2020
print([A029837(n) for n in range(1,31)])
