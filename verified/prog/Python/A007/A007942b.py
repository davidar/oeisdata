def A007942(n): return int(''.join(map(str,range(n,1,-1)))+''.join(map(str,range(1,n+1)))) # _Chai Wah Wu_, Mar 21 2023
print([A007942(n) for n in range(1,31)])
