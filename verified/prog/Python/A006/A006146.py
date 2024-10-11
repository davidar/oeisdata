from sympy import primefactors
def aupton(terms):
  alst, k, sopfk, sopfkp1 = [], 0, 0, 1
  while len(alst) < terms:
    k, sopfk, sopfkp1 = k+1, sopfkp1, sum(p for p in primefactors(k+1))
    if sopfkp1 == sopfk: alst.append(sopfk)
  return alst
print(aupton(58)) # _Michael S. Branicky_, May 05 2021