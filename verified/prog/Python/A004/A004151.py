def A004151(n):
    a, b = divmod(n,10)
    while not b:
        n = a
        a, b = divmod(n,10)
    return n # _Chai Wah Wu_, Feb 20 2024
print([A004151(n) for n in range(1,31)])
