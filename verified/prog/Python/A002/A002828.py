from sympy import factorint
def A002828(n):
    if n == 0: return 0
    f = factorint(n).items()
    if not any(e&1 for p,e in f): return 1
    if all(p&3<3 or e&1^1 for p,e in f): return 2
    return 3+(((m:=(~n&n-1).bit_length())&1^1)&int((n>>m)&7==7)) # _Chai Wah Wu_, Aug 01 2023
print([A002828(n) for n in range(30)])
