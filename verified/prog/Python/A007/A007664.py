from math import isqrt
def A007664(n): return (1<<(r:=(k:=isqrt(m:=n+1<<1))+int(m>=k*(k+1)+1)-1))*(n-1-(r*(r-1)>>1))+1 # _Chai Wah Wu_, Oct 17 2022
print([A007664(n) for n in range(30)])
