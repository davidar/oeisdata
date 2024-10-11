from sympy import sieve
A000006 = lambda n: int(sieve[n]**.5)
print([A000006(n) for n in range(1,100+1)])
# _Albert Lahat_, Jun 25 2020