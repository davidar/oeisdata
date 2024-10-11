from sympy import primerange
def aupto(limit):
  p, q, r, alst = 2, 3, 5, []
  for s in primerange(7, limit+9):
    if p+2 == q and p+6 == r and p+8 == s: alst.append(p)
    p, q, r = q, r, s
  return alst
print(aupto(10**5)) # _Michael S. Branicky_, May 11 2021