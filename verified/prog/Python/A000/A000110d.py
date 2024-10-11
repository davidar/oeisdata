from functools import cache
@cache
def a(n, k=0): return int(n < 1) or k*a(n-1, k) + a(n-1, k+1)
print([a(n) for n in range(27)])  # _Peter Luschny_, Jun 14 2022