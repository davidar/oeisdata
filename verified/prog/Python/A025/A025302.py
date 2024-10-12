from collections import Counter
from itertools import combinations
def aupto(lim):
  s = filter(lambda x: x <= lim, (i*i for i in range(1, int(lim**.5)+2)))
  s2 = filter(lambda x: x <= lim, (sum(c) for c in combinations(s, 2)))
  s2counts = Counter(s2)
  return sorted(k for k in s2counts if k <= lim and s2counts[k] == 1)
print(aupto(229)) # _Michael S. Branicky_, May 10 2021