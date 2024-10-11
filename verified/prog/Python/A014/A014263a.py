from sympy.ntheory.digits import digits
def a(n): return int(''.join(str(2*d) for d in digits(n, 5)[1:]))
print([a(n) for n in range(58)]) # _Michael S. Branicky_, Jan 13 2022