from math import isqrt
def A030140(n): return (n+(k:=isqrt(n))+int(n>=k*(k+1)+1))**2 # _Chai Wah Wu_, Jun 17 2024
print([A030140(n) for n in range(1,31)])
