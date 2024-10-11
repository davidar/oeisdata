from sympy import isprime
from itertools import product
def pals(d, base=10): # all d-digit palindromes
    digits = "".join(str(i) for i in range(base))
    for p in product(digits, repeat=d//2):
        if d > 1 and p[0] == "0": continue
        left = "".join(p); right = left[::-1]
        for mid in [[""], digits][d%2]: yield int(left + mid + right)
def a(n): return int(n==2) if n%2 == 0 else sum(isprime(p) for p in pals(n))
print([a(n) for n in range(1, 13)]) # _Michael S. Branicky_, Jun 23 2021