from sympy import divisors, totient
l=[0, 1]
for n in range(2, 101):
    l.append(sum([totient(n//d)*l[d] for d in divisors(n)[:-1]]))
print(l[1:]) # _Indranil Ghosh_, Jul 12 2017