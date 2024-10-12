def A029883(n): return (bin(n).count('1')&1)-(bin(n-1).count('1')&1) # _Chai Wah Wu_, Mar 03 2023
print([A029883(n) for n in range(1,31)])
