def A028909(n):
    return int(''.join(sorted(str(2**n)))) # _Chai Wah Wu_, Feb 19 2021
print([A028909(n) for n in range(30)])
