from sympy import var, diff
x = var('x')
y = x**x
l = [[y:=diff(y),y.subs(x,1)/(n+1)][1] for n in range(10)]
print(l) # _Nicholas Stefan Georgescu_, Mar 02 2023