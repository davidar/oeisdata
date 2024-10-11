from sympy import factorint
def A003415(n):
    return sum([int(n*e/p) for p,e in factorint(n).items()]) if n > 1 else 0
# _Chai Wah Wu_, Aug 21 2014
print([A003415(n) for n in range(30)])
