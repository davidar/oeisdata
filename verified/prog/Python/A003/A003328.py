from collections import Counter
from itertools import combinations_with_replacement as combs_w_rep
def aupto(lim):
  s = filter(lambda x: x<=lim, (i**3 for i in range(1, int(lim**(1/3))+2)))
  s2 = filter(lambda x: x<=lim, (sum(c) for c in combs_w_rep(s, 5)))
  s2counts = Counter(s2)
  return sorted(k for k in s2counts)
print(aupto(200)) # _Michael S. Branicky_, May 12 2021