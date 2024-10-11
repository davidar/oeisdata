from sympy import fibonacci
def a(n):
    k=0
    x=0
    while n>0:
        k=0
        while fibonacci(k)<=n: k+=1
        x+=10**(k - 3)
        n-=fibonacci(k - 1)
    return str(x).count("1")
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 09 2017