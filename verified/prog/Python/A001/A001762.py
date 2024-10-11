from math import factorial
from sympy import binomial
def a(n):
    if n < 4:
        return 1
    else:
        return binomial(n, 3) * factorial(3*n-9) // factorial(2*n-4)
print([a(n) for n in range(3, 21)]) # _Paul Muljadi_, Mar 05 2024