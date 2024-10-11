def A004520(n):
    return int(''.join(str(2*int(d) % 10) for d in str(n))) # _Chai Wah Wu_, Jun 29 2020
print([A004520(n) for n in range(30)])
