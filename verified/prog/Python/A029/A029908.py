from sympy import factorint
def a(n, pn):
    if n == pn:
        return n
    else:
        return a(sum(p*e for p, e in factorint(n).items()), n)
print([a(i, None) for i in range(1, 100)]) # _Gleb Ivanov_, Nov 05 2021