# see link for faster version
limit = 1664
from functools import lru_cache
sq = [k*k for k in range(1, int(limit**.5)+2) if k*k + 3 <= limit]
sqs = set(sq)
@lru_cache(maxsize=None)
def findsums(n, m):
  if m == 1: return {(n,)} if n in sqs else set()
  return set(tuple(sorted(t+(s, ))) for s in sq for t in findsums(n-s, m-1))
print([n for n in range(4, limit+1) if len(findsums(n, 4)) == 1]) # _Michael S. Branicky_, Apr 07 2021