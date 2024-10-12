def A004290(n):
    if n > 0:
        for i in range(1,2**n):
            x = int(bin(i)[2:])
            if not x % n:
                return x
    return 0
# _Chai Wah Wu_, Dec 30 2014
print([A004290(n) for n in range(1,31)])
