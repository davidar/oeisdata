from math import isqrt
def A001614(n): return (m:=n<<1)-(k:=isqrt(m))-int((m<<2)>(k<<2)*(k+1)+1) # _Chai Wah Wu_, Jul 26 2022
print([A001614(n) for n in range(1,31)])
