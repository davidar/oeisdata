from functools import lru_cache
@lru_cache(maxsize=None)
def F(n):
    if n == 0: return 8
    elif 3*F(n-1)%2 == 0: return 3*F(n-1)//2
    else: return (3*F(n-1)+1)//4
print([F(i) for i in range(81)]) # _Michael S. Branicky_, Aug 12 2021 after _J. H. Conway_