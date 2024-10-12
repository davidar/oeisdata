from functools import lru_cache
@lru_cache(maxsize=None)
def A000198(n):
    if n <= 7: return (1, 1, 3, 3, 5, 9, 21)[n-1]
    if (r:=n%9) in {0,3,6}:
        return 3**(m:=n//3)*A000198(m)
    elif r in {1,2,4}:
        return A000198(n-1)
    elif r == 5:
        return max(A000198(n-2),5*A000198(n-5),21*A000198(n-7))
    elif r == 7:
        return 21*A000198(n-7)
    elif r == 8:
        return max(A000198(n-1),5*A000198(n-5)) # _Chai Wah Wu_, Jul 01 2024
print([A000198(n) for n in range(1,31)])
