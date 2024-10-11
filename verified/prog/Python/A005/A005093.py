from sympy import divisors, fibonacci
l = [fibonacci(n) for n in range(1, 21)]
def a(n):
    return sum(i**2 for i in divisors(n) if i in l)
print([a(n) for n in range(1, 101)])  # _Indranil Ghosh_, Mar 22 2017