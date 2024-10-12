from sympy import euler
def A028296(n): return euler(n<<1) # _Chai Wah Wu_, Apr 16 2023
print([A028296(n) for n in range(30)])
