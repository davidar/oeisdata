from sympy import totient, gcd
def a(n):
    s=0
    k=2
    while s<n:
        s+=totient(k)
        k+=1
    s-=totient(k - 1)
    j=1
    while s<n:
        if gcd(j, k - 1)==1:
            s+=1
        j+=1
    return j - 1
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, May 23 2017, after Ulrich Schimke's MAPLE code