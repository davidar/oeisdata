from sympy import divisors, totient, mobius
l=[0, 0]
for n in range(2, 101):
    l.append(sum(totient(n//d)*sum(mobius(d//c)*2**(c - 1) for c in divisors(d)) for d in divisors(n)[:-1]))
print(l[1:]) # _Indranil Ghosh_, Jul 12 2017