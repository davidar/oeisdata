# Python 2.4 or higher required
from sympy import isprime
A002496_list = list(filter(isprime, (n*n+1 for n in range(10**5)))) # _David Radcliffe_, Jun 26 2016
print(A002496_list)
