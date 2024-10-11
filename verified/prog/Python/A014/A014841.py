from sympy.ntheory import digits
def a(n): return sum(sum(digits(n, b)[1:])%b for b in range(2, n))
print([a(n) for n in range(3, 60)]) # _Michael S. Branicky_, Sep 06 2022