from sympy import sqrt
from sympy.ntheory.continued_fraction import continued_fraction_iterator
def aupton(terms):
    gen = continued_fraction_iterator(sqrt(107))
    return [next(gen) for i in range(terms)]
print(aupton(82)) # _Michael S. Branicky_, Oct 02 2021