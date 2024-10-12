from sympy import isprime
def alst():
  primes, alst = [2, 3, 5, 7], []
  while len(primes) > 0:
    alst += sorted(primes)
    candidates = set(int(d+str(p)) for p in primes for d in "123456789")
    primes = [c for c in candidates if isprime(c)]
  return alst
print(alst()) # _Michael S. Branicky_, Apr 11 2021