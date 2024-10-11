from math import prod
def f(x): return x + prod(map(int, str(x)))
def a(n):
    x, fx = n, f(n)
    while x != fx: x, fx = fx, f(fx)
    return x
print([a(n) for n in range(60)]) # _Michael S. Branicky_, Jun 21 2022