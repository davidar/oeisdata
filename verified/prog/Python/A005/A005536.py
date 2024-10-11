from sympy.ntheory import digits
def A005536(n): return sum(sum((0,1,-1,0)[i] for i in digits(m,4)[1:]) for m in range(n+1)) # _Chai Wah Wu_, Jul 19 2024
print([A005536(n) for n in range(30)])
