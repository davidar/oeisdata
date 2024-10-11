limit = 10026 # 10000th term in b-file
from functools import lru_cache
nzs = [k*k for k in range(1, int(limit**.5)+2) if k*k + 3 <= limit]
nzss = set(nzs)
@lru_cache(maxsize=None)
def ok(n, m): return n in nzss if m == 1 else any(ok(n-s, m-1) for s in nzs)
print([n for n in range(4, limit+1) if ok(n, 4)]) # _Michael S. Branicky_, Apr 07 2021