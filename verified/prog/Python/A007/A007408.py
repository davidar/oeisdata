from fractions import Fraction
from itertools import accumulate, count, islice
def A007408gen(): yield from map(lambda x: x.numerator, accumulate(Fraction(1, k**3) for k in count(1)))
print(list(islice(A007408gen(), 20))) # _Michael S. Branicky_, Jun 26 2022