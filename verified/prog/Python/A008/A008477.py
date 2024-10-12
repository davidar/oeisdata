from sympy import factorint, prod
a = lambda n: prod([pk[1]**pk[0] for pk in factorint(n).items()])
print([a(n) for n in range(1,61)]) # _Darío Clavijo_, Nov 06 2023