from sympy import sieve
def A018805(n): return 2*sum(t for t in sieve.totientrange(1,n+1)) - 1 # _Chai Wah Wu_, Mar 23 2021
print([A018805(n) for n in range(1,31)])
