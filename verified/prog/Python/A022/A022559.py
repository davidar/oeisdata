from sympy import factorint as pf
def aupton(nn):
    alst = [0]
    for n in range(1, nn+1): alst.append(alst[-1] + sum(pf(n).values()))
    return alst
print(aupton(63)) # _Michael S. Branicky_, Aug 01 2021