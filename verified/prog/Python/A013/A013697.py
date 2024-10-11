from sympy import zeta
print([1//(zeta(n) - 1) for n in range(2, 32)]) # _Karl V. Keller, Jr._, Jul 21 2020