from sympy import primerange
p = lambda x: list(primerange(x, x+10)); A024770 = p(0); i=0
while i<len(A024770): A024770+=p(A024770[i]*10); i+=1 # _M. F. Hasler_, Mar 11 2020
print(A024770)
