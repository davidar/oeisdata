from sympy import factorint
def a(n):
    if n == 0: return 1
    an = 4
    for pi, ei in factorint(n).items():
       if pi%4 == 1: an *= ei+1
       elif pi%4 == 3 and ei%2: return 0
    return an
print([a(n) for n in range(102)]) # _Michael S. Branicky_, Sep 24 2021