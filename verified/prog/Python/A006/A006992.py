from sympy import prevprime
l = [2]
for i in range(1, 51):
    l.append(prevprime(2 * l[i - 1]))
print(l) # _Indranil Ghosh_, Apr 26 2017