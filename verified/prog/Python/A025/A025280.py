from math import gcd
from sympy import divisors, factorint, integer_nthroot
from functools import cache
@cache
def a(n):
    if n == 1: return 1
    p = min(a(i)+a(n-1) for i in range(1, n//2+1))
    divs, m = divisors(n), n
    if len(divs) > 2:
        m = min(a(d)+a(n//d) for d in divs[1:len(divs)//2+1])
    f = factorint(n)
    edivs, e = divisors(gcd(*f.values())), n
    if len(edivs) > 1:
        e = min(a(integer_nthroot(n, r)[0])+a(r) for r in edivs[1:])
    return min(p, m, e)
print([a(n) for n in range(1, 88)]) # _Michael S. Branicky_, Mar 24 2024 after _Alois P. Heinz_