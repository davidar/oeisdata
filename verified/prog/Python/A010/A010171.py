from sympy import sqrt
from sympy.ntheory.continued_fraction import continued_fraction_iterator
def aupton(terms):
    gen = continued_fraction_iterator(sqrt(103))
    return [next(gen) for i in range(terms)]
print(aupton(85)) # _Michael S. Branicky_, Oct 06 2021