from sympy.ntheory.continued_fraction import continued_fraction_periodic
def a(n):
    cfp = continued_fraction_periodic(0, 1, d=n)
    return 0 if len(cfp) == 1 else len(cfp[1])
print([a(n) for n in range(1, 104)]) # _Michael S. Branicky_, Aug 22 2021