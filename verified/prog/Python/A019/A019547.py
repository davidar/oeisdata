from math import isqrt
def issquare(n): return isqrt(n)**2 == n
def ok(n, c):
    if n%10 in { 2, 3, 7, 8}: return False
    if issquare(n) and c > 1: return True
    d = str(n)
    for i in range(1, len(d)):
        if issquare(int(d[:i])) and ok(int(d[i:]), c+1): return True
    return False
print([r*r for r in range(180) if ok(r*r, 1)]) # _Michael S. Branicky_, Jul 10 2021