from sympy import divisors
def a(n): return 1 if n==0 else 8*sum(d for d in divisors(n) if d%4 != 0)
print([a(n) for n in range(57)]) # _Michael S. Branicky_, Jan 08 2021