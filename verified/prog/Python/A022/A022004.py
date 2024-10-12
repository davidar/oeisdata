from sympy import primerange
def aupto(limit):
  p, q, alst = 2, 3, []
  for r in primerange(5, limit+7):
    if p+2 == q and p+6 == r: alst.append(p)
    p, q = q, r
  return alst
print(aupto(5477)) # _Michael S. Branicky_, May 11 2021