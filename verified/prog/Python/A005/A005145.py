from sympy import primerange
a = []; [a.extend([pn]*n) for n, pn in enumerate(primerange(1, 32), 1)]
print(a) # _Michael S. Branicky_, Jul 13 2022