from sympy.functions.combinatorial.numbers import stirling
def A009454(n): return sum(stirling(n,(k<<1)+1,kind=1,signed=True)*(-1 if k&1 else 1) for k in range(n+1>>1)) # _Chai Wah Wu_, Feb 22 2024
print([A009454(n) for n in range(30)])
