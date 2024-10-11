from sympy.ntheory.factor_ import digits
print([n for n in range(201) if digits(n, 5)[1:].count(4)==0]) # _Indranil Ghosh_, May 23 2017