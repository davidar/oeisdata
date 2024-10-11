from sympy import isprime
from sympy.utilities.iterables import multiset_permutations
def aupton(terms):
  n, digits, alst = 0, 1, []
  while len(alst) < terms:
    mpstr = "".join(d*digits for d in "57")
    for mp in multiset_permutations(mpstr, digits):
      t = int("".join(mp))
      if isprime(t): alst.append(t)
      if len(alst) == terms: break
    else: digits += 1
  return alst
print(aupton(33)) # _Michael S. Branicky_, May 07 2021