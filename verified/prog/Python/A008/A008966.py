from sympy import factorint
def A008966(n): return int(max(factorint(n).values(),default=1)==1) # _Chai Wah Wu_, Apr 05 2023
print([A008966(n) for n in range(1,31)])
