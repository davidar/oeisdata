from math import isqrt
def A003056(n): return (k:=isqrt(m:=n+1<<1))+int((m<<2)>(k<<2)*(k+1)+1)-1 # _Chai Wah Wu_, Jul 26 2022
print([A003056(n) for n in range(30)])
