from fractions import Fraction
def a(n): return sum(Fraction(1, i) for i in range(1, n+1)).denominator
print([a(n) for n in range(1, 30)]) # _Michael S. Branicky_, Dec 24 2021