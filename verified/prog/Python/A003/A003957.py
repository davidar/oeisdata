from sympy import Symbol, nsolve, cos
x = Symbol("x")
a = list(map(int, str(nsolve(cos(x)-x, 1, prec=110))[2:-2]))
print(a) # _Michael S. Branicky_, Jul 15 2022