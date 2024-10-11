from sympy import isprime
print(list(filter(isprime, (n**2 + n + 1 for n in range(150))))) # _Michael S. Branicky_, Apr 20 2022