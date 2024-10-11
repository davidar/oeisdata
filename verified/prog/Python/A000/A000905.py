from sympy import binomial
a = [2]
[a.append(2+sum((-1)**(i)*binomial(a[n-i-1], i+2) for i in range(n))) for n in range(1,11)]
print(a) # _Nicholas Stefan Georgescu_, Mar 01 2023