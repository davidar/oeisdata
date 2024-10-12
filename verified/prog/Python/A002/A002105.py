from sympy import bernoulli
def A002105(n): return abs(((2-(2<<(m:=n<<1)))*bernoulli(m)<<n-1)//n) # _Chai Wah Wu_, Apr 14 2023
print([A002105(n) for n in range(1,31)])
