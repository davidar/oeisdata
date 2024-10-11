from functools import cache
@cache
def A005043(n: int) -> int:
    if n <= 1: return 1 - n
    return (n - 1) * (2 * A005043(n - 1) + 3 * A005043(n - 2)) // (n + 1)
print([A005043(n) for n in range(32)]) # _Peter Luschny_, Nov 20 2022