from sympy import catalan
def a244160(n):
    if n==0: return 0
    i=1
    while True:
        if catalan(i)>n: break
        else: i+=1
    return i - 1
def a(n):
    if n==0: return 0
    x=a244160(n)
    return 10**(x - 1) + a(n - catalan(x))
print([a(n) for n in range(51)]) # _Indranil Ghosh_, Jun 08 2017