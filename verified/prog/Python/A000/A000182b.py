from sympy import bernoulli
def A000182(n): return abs(((2-(2<<(m:=n<<1)))*bernoulli(m)<<m-2)//n) # _Chai Wah Wu_, Apr 14 2023
print([A000182(n) for n in range(1,31)])
