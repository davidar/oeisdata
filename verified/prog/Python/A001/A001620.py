from sympy import S
def aupton(digs): return [int(d) for d in str(S.EulerGamma.n(digs+2))[2:-2]]
print(aupton(99)) # _Michael S. Branicky_, Nov 22 2021