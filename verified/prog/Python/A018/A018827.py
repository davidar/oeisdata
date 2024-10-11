from sympy.ntheory import digits
def s(n, base=3): return "".join(map(str, digits(n, base)[1:]))
def ok(n): return s(n) in s(n**2)
print([k for k in range(10**5) if ok(k)]) # _Michael S. Branicky_, Apr 04 2024