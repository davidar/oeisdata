from sympy import isprime, nextprime
def ok(p): return isprime(2*p+1)
def aupto(limit): # only test primes
  alst, p = [], 2
  while p <= limit:
    if ok(p): alst.append(p)
    p = nextprime(p)
  return alst
print(aupto(1559)) # _Michael S. Branicky_, Feb 03 2021