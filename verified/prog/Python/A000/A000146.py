from fractions import Fraction
from sympy import bernoulli, divisors, isprime
def A000146(n): return int(bernoulli(m:=n<<1)+sum(Fraction(1,d+1) for d in divisors(m,generator=True) if isprime(d+1))) # _Chai Wah Wu_, Apr 14 2023
print([A000146(n) for n in range(1,31)])
