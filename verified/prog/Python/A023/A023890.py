from sympy import isprime
def A023890(n):
    s=0
    for i in range(1,n+1):
        if n%i==0 and not isprime(i):
            s+=i
    return s # _Indranil Ghosh_, Jan 30 2017
print([A023890(n) for n in range(1,31)])
