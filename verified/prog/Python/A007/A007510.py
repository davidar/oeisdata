from sympy import nextprime
def aupto(limit):
  n, p, q = 1, 2, 3
  alst, non_twins, twins = [], [2], [3]
  while True:
    p, q = q, nextprime(q)
    if q - p == 2:
      if p != twins[-1]: twins.append(p)
      twins.append(q)
    else:
      if p != twins[-1]: non_twins.append(p)
    if q > limit: return non_twins
print(aupto(563)) # _Michael S. Branicky_, Feb 23 2021