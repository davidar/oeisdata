def A005418(n): return 1 if n == 1 else 2**((m:= n//2)-1)*(2**(n-m-1)+1) # _Chai Wah Wu_, Feb 03 2022
print([A005418(n) for n in range(1,31)])
