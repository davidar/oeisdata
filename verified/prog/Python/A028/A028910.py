def A028910(n):
    return int(''.join(sorted(str(2**n),reverse=True))) # _Chai Wah Wu_, Feb 19 2021
print([A028910(n) for n in range(30)])
