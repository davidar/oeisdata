# faster for producing initial segment of sequence
from math import prod
from sympy import factorint
def ok(n):
    f = factorint(n)
    sigma1 = prod((p**(  e+1)-1)//(p-1)    for p, e in f.items())
    sigma2 = prod((p**(2*e+2)-1)//(p**2-1) for p, e in f.items())
    return sigma2%sigma1 ==  0
print([k for k in range(1, 1300) if ok(k)]) # _Michael S. Branicky_, Feb 25 2024