from functools import cache
@cache
def F(k, n):
    return sum(F(k, n-j) for j in range(1, min(k, n))) if n > 1 else n
def A007059(n): return sum(F(k, n+1-k) for k in range(1, n+1))
print([A007059(n) for n in range(36)])  # _Peter Luschny_, Jan 05 2024