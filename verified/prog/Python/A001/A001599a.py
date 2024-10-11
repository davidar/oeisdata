from sympy import divisor_sigma as sigma
def ok(n): return (n*sigma(n, 0))%sigma(n, 1) == 0
print([n for n in range(1, 10**4) if ok(n)]) # _Michael S. Branicky_, Jan 06 2021