from sympy import primerange
def aupto(limit):
  p, q, r, s, alst = 2, 3, 5, 7, []
  for t in primerange(11, limit+13):
    if p+2 == q and p+6 == r and p+8 == s and p+12 == t: alst.append(p)
    p, q, r, s = q, r, s, t
  return alst
print(aupto(10**6)) # _Michael S. Branicky_, May 11 2021