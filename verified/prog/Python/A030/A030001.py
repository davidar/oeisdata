def a(n):
  k, strn = 0, str(n)
  while strn not in str(2**k): k += 1
  return 2**k
print([a(n) for n in range(36)]) # _Michael S. Branicky_, Apr 03 2024