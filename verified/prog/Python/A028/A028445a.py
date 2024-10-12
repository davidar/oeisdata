from itertools import product
def cf(s):
    for l in range(1, len(s)//3 + 1):
      for i in range(len(s) - 3*l + 1):
          if s[i:i+l] == s[i+l:i+2*l] == s[i+2*l:i+3*l]: return False
    return True
def a(n):
    if n == 0: return 1
    return 2*sum(1 for w in product("01", repeat=n-1) if cf("0"+"".join(w)))
print([a(n) for n in range(21)]) # _Michael S. Branicky_, Mar 13 2022