from sympy import divisor_count
def ok(n): return divisor_count(n) == 6
print([k for k in range(429) if ok(k)]) # _Michael S. Branicky_, Dec 18 2021