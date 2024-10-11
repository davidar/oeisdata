from sympy import primefactors
A007774_list = [n for n in range(1,10**5) if len(primefactors(n)) == 2] # _Chai Wah Wu_, Aug 23 2021
print(A007774_list)
