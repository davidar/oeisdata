limit = 1218
from functools import lru_cache
qd = [k**4 for k in range(1, int(limit**.25)+2) if k**4 + 3 <= limit]
qds = set(qd)
@lru_cache(maxsize=None)
def findsums(n, m):
  if m == 1: return {(n, )} if n in qds else set()
  return set(tuple(sorted(t+(q,))) for q in qds for t in findsums(n-q, m-1))
print([n for n in range(4, limit+1) if len(findsums(n, 4)) >= 1]) # _Michael S. Branicky_, Apr 19 2021