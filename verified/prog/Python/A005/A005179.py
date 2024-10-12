from math import prod
from sympy import isprime, divisors, prime
def A005179(n):
    def mult_factors(n):
        if isprime(n):
            return [(n,)]
        c = []
        for d in divisors(n,generator=True):
            if 1<d<n:
                for a in mult_factors(n//d):
                    c.append(tuple(sorted((d,)+a)))
        return list(set(c))
    return min((prod(prime(i)**(j-1) for i,j in enumerate(reversed(d),1)) for d in mult_factors(n)),default=1) # _Chai Wah Wu_, Aug 17 2024
print([A005179(n) for n in range(1,31)])
