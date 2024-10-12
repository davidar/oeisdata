from sympy import factorint, primefactors
def a053585(n):
    if n==1: return 1
    p = primefactors(n)[-1]
    return p**factorint(n)[p]
print([n for n in range(2, 301) if n>a053585(n)*primefactors(n)[-1]]) # _Indranil Ghosh_, Jul 13 2017