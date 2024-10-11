from functools import lru_cache
@lru_cache(maxsize=None)
def A006046(n):return n if n<=1 else 2*A006046((n-1)//2)+A006046((n+1)//2)if n%2 else 3*A006046(n//2) # _Guillermo Hernández_, Dec 31 2023
print([A006046(n) for n in range(30)])
