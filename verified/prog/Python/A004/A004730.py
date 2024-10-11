from sympy import gcd, factorial2
def A004730(n):
    a, b = factorial2(n), factorial2(n+1)
    return a//gcd(a,b) # _Chai Wah Wu_, Apr 03 2021
print([A004730(n) for n in range(30)])
