from collections import Counter
from itertools import combinations_with_replacement as multi_combs
def aupto(lim):
  c = filter(lambda x: x<=lim, (i**3 for i in range(1, int(lim**(1/3))+2)))
  s = filter(lambda x: x<=lim, (sum(mc) for mc in multi_combs(c, 6)))
  counts = Counter(s)
  return sorted(k for k in counts)
print(aupto(170)) # _Michael S. Branicky_, Jun 13 2021