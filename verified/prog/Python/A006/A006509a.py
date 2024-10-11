from sympy import primerange, prime
def aupton(terms):
  alst = [1]
  for n, pn in enumerate(primerange(1, prime(terms)+1), start=1):
    x, y = alst[-1] - pn, alst[-1] + pn
    if x > 0 and x not in alst: alst.append(x)
    elif y > 0 and y not in alst: alst.append(y)
    else: alst.append(0)
  return alst
print(aupton(130)) # _Michael S. Branicky_, May 30 2021