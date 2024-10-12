from math import isqrt
def A024920(n): return (s:=isqrt(n))**2*(s+1-(n<<1))+sum((q:=n//k)*((n<<2)-(k<<1)-q-1) for k in range(1,s+1))>>1 # _Chai Wah Wu_, Oct 23 2023
print([A024920(n) for n in range(1,31)])
