from sympy import sqrt
from sympy.ntheory.continued_fraction import continued_fraction_iterator
def aupton(nn):
    gen = continued_fraction_iterator(sqrt(149))
    return [next(gen) for i in range(nn+1)]
print(aupton(83)) # _Michael S. Branicky_, Dec 04 2021