from sympy import nextprime
def ispal(n): s = str(n); return s == s[::-1]
def aupto(lim):
  prevp, p, alst = 2, 3, []
  while p < lim:
    if ispal(p * prevp): alst.append(p)
    prevp, p = p, nextprime(p)
  return alst
print(aupto(2*10**6)) # _Michael S. Branicky_, Mar 11 2021