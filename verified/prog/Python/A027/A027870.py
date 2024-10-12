def A027870(n):
    return str(2**n).count('0') # _Chai Wah Wu_, Feb 14 2020
print([A027870(n) for n in range(30)])
