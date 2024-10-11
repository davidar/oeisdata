from sympy import factorint
def A014963(n):
    y = factorint(n)
    return list(y.keys())[0] if len(y) == 1 else 1
print([A014963(n) for n in range(1, 71)]) # _Chai Wah Wu_, Sep 04 2014