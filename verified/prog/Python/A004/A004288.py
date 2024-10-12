def A004288(n):
    if n > 0:
        for i in range(1, 2**n):
            s = bin(i)[2:]
            if not int(s,8) % n:
                return int(s)
    return 0 # _Chai Wah Wu_, Dec 30 2014
print([A004288(n) for n in range(1,31)])
