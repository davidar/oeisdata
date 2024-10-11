from math import comb, isqrt
def a(n): return n - comb((1+isqrt(8+8*n))//2, 2)
print([a(n) for n in range(105)]) # _Michael S. Branicky_, May 07 2023