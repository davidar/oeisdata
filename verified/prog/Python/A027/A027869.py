from math import factorial
def a(n): return str(factorial(n)).count('0')
print([a(n) for n in range(74)]) # _Michael S. Branicky_, Jan 11 2022