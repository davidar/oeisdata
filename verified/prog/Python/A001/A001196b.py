from itertools import groupby
def ok2lb(n):
  if n == 0: return True  # by convention
  return all(len(list(g))%2 == 0 for k, g in groupby(bin(n)[2:]))
print([i for i in range(3313) if ok2lb(i)]) # _Michael S. Branicky_, Jan 04 2021