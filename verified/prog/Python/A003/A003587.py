def f(s, k):
    return s[:2] if k==4 else (s[1]*(k>=5)+s[0]*(k%5) if k<9 else s[0]+s[2])
def roman(n):
    m, c, x, i = n//1000, (n%1000)//100, (n%100)//10, n%10
    return "M"*m + f("CDM", c) + f("XLC", x) + f("IVX", i)
def afull():
    return sorted(list(range(1, 4000)), key=lambda x: (len(roman(x)), x))
print(afull()) # _Michael S. Branicky_, Dec 04 2022