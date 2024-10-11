from sympy import factorint
def aupton(terms):
  alst, k, sopfk, sopfkp1 = [], 2, 2, 3
  while len(alst) < terms:
    if sopfkp1 == sopfk: alst.append(k)
    k, sopfk, sopfkp1 = k+1, sopfkp1, sum(p for p in factorint(k+2))
  return alst
print(aupton(42)) # _Michael S. Branicky_, May 24 2021