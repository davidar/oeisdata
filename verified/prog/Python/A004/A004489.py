def T(n, m):
  k, pow3 = 0, 1
  while n + m > 0:
    n, rn = divmod(n, 3)
    m, rm = divmod(m, 3)
    k, pow3 = k + pow3*((rn+rm)%3), pow3*3
  return k
print([T(n, d-n) for d in range(14) for n in range(d+1)]) # _Michael S. Branicky_, May 04 2021