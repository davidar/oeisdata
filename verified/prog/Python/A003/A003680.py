from sympy import divisors
def a(n):
  m = 4*n - 2
  while len(divisors(m)) != 2*n: m += 1
  return m
print([a(n) for n in range(1, 19)]) # _Michael S. Branicky_, Feb 06 2021