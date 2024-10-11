from sympy.ntheory.factor_ import digits
def a(n): return int("".join([str((3 - i)%3) for i in digits(n, 3)[1:]]), 3) # _Indranil Ghosh_, Jun 06 2017
print([a(n) for n in range(30)])
