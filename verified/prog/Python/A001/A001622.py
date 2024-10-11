from sympy import S
def alst(n): # truncate extra last digit to avoid rounding
  return list(map(int, str(S.GoldenRatio.n(n+1)).replace(".", "")))[:-1]
print(alst(105)) # _Michael S. Branicky_, Jan 06 2021