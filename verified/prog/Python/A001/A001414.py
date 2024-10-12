from sympy import factorint
def A001414(n):
    return sum(p*e for p,e in factorint(n).items()) # _Chai Wah Wu_, Jan 08 2016
print([A001414(n) for n in range(1,31)])
