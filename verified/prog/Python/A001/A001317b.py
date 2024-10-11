def A001317(n): return int(''.join(str(int(not(~n&k))) for k in range(n+1)),2) # _Chai Wah Wu_, Feb 04 2022
print([A001317(n) for n in range(30)])
