from sympy import gcd, factorial2
def A004731(n):
    if n <= 1:
        return 1
    a, b = factorial2(n-2), factorial2(n-1)
    return b//gcd(a,b) # _Chai Wah Wu_, Apr 03 2021
print([A004731(n) for n in range(30)])
