from sympy import binomial
A000475_list, m, x = [], 1, 0
for n in range(4,100):
    x, m = x*n + m*binomial(n,4), -m
    A000475_list.append(x) # _Chai Wah Wu_, Nov 01 2014
print(A000475_list)
