from sympy import isprime
A020449_list = [n for n in (int(format(m,'b')) for m in range(1,2**10)) if isprime(n)] # _Chai Wah Wu_, Dec 17 2015
print(A020449_list)
