from sympy import prime, primerange
def aupton(nn):
    alst, prevp = [], 2
    for p in primerange(3, prime(nn+1)+1): alst.append(prevp*p); prevp = p
    return alst
print(aupton(43)) # _Michael S. Branicky_, Jun 15 2021