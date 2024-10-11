# much faster version for initial segment of sequence
from sympy import nextprime, isprime
def aupton(terms):
    alst, p, pi = [], 2, 1
    while len(alst) < terms:
        if isprime(pi): alst.append(p)
        p, pi = nextprime(p), pi+1
    return alst
print(aupton(10000)) # _Michael S. Branicky_, Aug 11 2021