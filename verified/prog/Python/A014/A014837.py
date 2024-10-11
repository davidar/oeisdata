from sympy.ntheory.digits import digits
def a(n): return sum(sum(digits(n, b)[1:]) for b in range(2, n))
print([a(n) for n in range(3, 59)]) # _Michael S. Branicky_, Apr 04 2022