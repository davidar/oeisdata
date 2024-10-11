from sympy import sqrt
from sympy.ntheory.continued_fraction import continued_fraction_iterator
def aupton(terms):
    gen = continued_fraction_iterator(sqrt(86))
    return [next(gen) for i in range(terms)]
print(aupton(78)) # _Michael S. Branicky_, Sep 03 2021