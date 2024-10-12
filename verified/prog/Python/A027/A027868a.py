from sympy import multiplicity
A027868, p5 = [0,0,0,0,0], 0
for n in range(5,10**3,5):
    p5 += multiplicity(5,n)
    A027868.extend([p5]*5) # _Chai Wah Wu_, Sep 05 2014
print(A027868)
