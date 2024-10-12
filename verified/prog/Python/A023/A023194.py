from sympy import isprime, divisor_sigma
A023194_list = [2]+[n**2 for n in range(1,10**3) if isprime(divisor_sigma(n**2))] # _Chai Wah Wu_, Jul 14 2016
print(A023194_list)
