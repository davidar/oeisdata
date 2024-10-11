# via recursion
from functools import lru_cache
@lru_cache(maxsize=None)
def a(n): return 0 if n == 0 else (a((n-1)//2)+1 if n%2 else -a(n//2))
print([a(n) for n in range(86)]) # _Michael S. Branicky_, Apr 03 2021