from sympy import factorint
def sd(n): return sum(map(int, str(n)))
def ok(n):
  f = factorint(n)
  return sum(f[p] for p in f) > 1 and sd(n) == sum(sd(p)*f[p] for p in f)
print(list(filter(ok, range(1220)))) # _Michael S. Branicky_, Apr 22 2021