def ispal(s): return s == s[::-1]
def ok(n): return ispal(str(n**3))
print([k for k in range(10**7) if ok(k)]) # _Michael S. Branicky_, Aug 02 2022