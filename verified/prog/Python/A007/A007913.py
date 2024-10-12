from sympy import factorint, prod
def A007913(n):
    return prod(p for p, e in factorint(n).items() if e % 2)
# _Chai Wah Wu_, Feb 03 2015
print([A007913(n) for n in range(1,31)])
