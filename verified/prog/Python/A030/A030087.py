from sympy import isprime
A030087_list = [n for n in range(1,10**6) if set(str(n)) & set(str(n**3)) == set() and isprime(n)]
# _Chai Wah Wu_, Jan 05 2015
print(A030087_list)
