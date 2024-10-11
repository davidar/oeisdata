def A004167(n):
    return int(str(3**n)[::-1]) # _Chai Wah Wu_, Feb 19 2021
print([A004167(n) for n in range(30)])
