from math import isqrt
def A011550(n): return (m:=isqrt(k:=10**(n<<1)*3))+int((k-m*(m+1)<<2)>=1) # _Chai Wah Wu_, Jul 29 2022
print([A011550(n) for n in range(30)])
