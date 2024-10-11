def A004185(n):
    return int(''.join(sorted(str(n))).replace('0','')) if n > 0 else 0 # _Chai Wah Wu_, Nov 10 2015
print([A004185(n) for n in range(30)])
