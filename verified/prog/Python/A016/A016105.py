from sympy import factorint
def ok(n):
    fn = factorint(n)
    return len(fn) == sum(fn.values()) == 2 and all(f%4 == 3 for f in fn)
print([k for k in range(790) if ok(k)]) # _Michael S. Branicky_, Dec 20 2021