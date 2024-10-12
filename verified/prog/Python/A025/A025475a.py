from sympy import primerange
A025475_list, m = [1], 10*2
m2 = m**2
for p in primerange(1,m):
    a = p**2
    while a < m2:
        A025475_list.append(a)
        a *= p
A025475_list = sorted(A025475_list) # _Chai Wah Wu_, Sep 08 2014
print(A025475_list)
