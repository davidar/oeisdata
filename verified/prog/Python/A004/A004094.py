def A004094(n):
    return int(str(2**n)[::-1]) # _Chai Wah Wu_, Feb 19 2021
print([A004094(n) for n in range(30)])
