from sympy import bernoulli
def A001469(n): return (2-(2<<(m:=n<<1)))*bernoulli(m) # _Chai Wah Wu_, Apr 14 2023
print([A001469(n) for n in range(1,31)])
