from sympy import factorial, isprime
A002982_list = [n for n in range(1,10**2) if isprime(factorial(n)-1)] # _Chai Wah Wu_, Apr 04 2021
print(A002982_list)
