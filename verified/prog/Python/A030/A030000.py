def a(n):
  k, strn = 0, str(n)
  while strn not in str(2**k): k += 1
  return k
print([a(n) for n in range(74)]) # _Michael S. Branicky_, Mar 06 2021