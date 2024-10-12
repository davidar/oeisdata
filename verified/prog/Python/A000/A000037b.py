from math import isqrt
def A000037(n): return n+(k:=isqrt(n))+int(n>=k*(k+1)+1) # _Chai Wah Wu_, Jun 17 2024
print([A000037(n) for n in range(1,31)])
