limit = 226
from functools import lru_cache
sq = [k**2 for k in range(1, int(limit**.5)+2) if k**2 + 3 <= limit]
sqs = set(sq)
@lru_cache(maxsize=None)
def findsums(n, m):
  if m == 1: return {(n, )} if n in sqs else set()
  return set(tuple(sorted(t+(s,))) for s in sqs for t in findsums(n-s, m-1))
print([n for n in range(4, limit+1) if len(findsums(n, 4)) >= 6]) # _Michael S. Branicky_, Apr 20 2021