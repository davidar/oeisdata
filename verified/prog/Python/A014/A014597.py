from math import factorial, isqrt
from itertools import chain, combinations
from sympy.ntheory.primetest import is_square
fac =[factorial(n) for n in range(1, 16)] # raise 16 to search higher
def powerset(s): # skipping empty set
  return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))
gen = (isqrt(sum(s)) for s in powerset(fac) if is_square(sum(s)))
print(sorted(set(gen))) # _Michael S. Branicky_, Jan 03 2021