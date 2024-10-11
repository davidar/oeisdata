from sympy import perfect_power
def ok(n): return n==1 or perfect_power(n)
print([m for m in range(1, 1765) if ok(m)]) # _Michael S. Branicky_, Jan 04 2021