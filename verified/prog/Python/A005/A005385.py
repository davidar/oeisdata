from sympy import isprime, primerange
def aupto(limit):
  alst = []
  for p in primerange(1, limit+1):
    if isprime((p-1)//2): alst.append(p)
  return alst
print(aupto(2963)) # _Michael S. Branicky_, May 07 2021