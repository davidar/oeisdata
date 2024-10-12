from sympy import isprime
print(list(filter(isprime, (3*k**2+6*k+5 for k in range(350))))) # _Michael S. Branicky_, May 29 2021