def f(s, k):
    return s[:2] if k==4 else (s[1]*(k>=5)+s[0]*(k%5) if k<9 else s[0]+s[2])
def a(n):
    m, c, x, i = n//1000, (n%1000)//100, (n%100)//10, n%10
    return len("M"*m + f("CDM", c) + f("XLC", x) + f("IVX", i))
print([a(n) for n in range(1, 101)]) # _Michael S. Branicky_, Mar 03 2024