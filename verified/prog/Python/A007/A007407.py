from fractions import Fraction
def A007407(n): return sum(Fraction(1,k**2) for k in range(1,n+1)).denominator # _Chai Wah Wu_, Apr 03 2021
print([A007407(n) for n in range(1,31)])
