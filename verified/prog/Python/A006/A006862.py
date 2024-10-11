from sympy import primorial
def A006862(n):
    if n == 0: return 2
    else: return 1 + primorial(n) # _Karl-Heinz Hofmann_, Aug 21 2024
print([A006862(n) for n in range(30)])
