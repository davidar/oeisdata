from sympy import nextprime
def aupton(terms):
  alst, p = [], 2
  for n in range(1, terms+1):
    s = 0
    for i in range(n):
      s += p
      p = nextprime(p)
    alst.append(s)
  return alst
print(aupton(40)) # _Michael S. Branicky_, Feb 08 2021