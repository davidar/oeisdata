def tersum(a, b):
  c, pow3 = 0, 1
  while a + b > 0:
    a, ra = divmod(a, 3)
    b, rb = divmod(b, 3)
    c, pow3 = c + pow3*((ra+rb)%3), pow3*3
  return c
def a(n): return tersum(n, 4)
print([a(n) for n in range(58)]) # _Michael S. Branicky_, Apr 05 2021