from math import isqrt, comb
def A004202(n): return n+comb((m:=isqrt(k:=n<<1))+(k-m*(m+1)>=1)+1,2) # _Chai Wah Wu_, Jun 19 2024
print([A004202(n) for n in range(1,31)])
