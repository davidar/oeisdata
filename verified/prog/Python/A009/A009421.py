from sympy import integer_nthroot
def iscube(n): return integer_nthroot(n, 3)[1]
def ok3(n, c):
    if n%10 == 9 or (c == 1 and n%10 == 0): return False
    if c > 1 and iscube(n): return True
    d = str(n)
    for i in range(1, len(d)):
        if iscube(int(d[:i])) and ok3(int(d[i:]), c+1): return True
    return False
print([r**3 for r in range(122000) if ok3(r**3, 1)]) # _Michael S. Branicky_, Jul 11 2021