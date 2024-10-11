from sympy import isprime, nextprime
def emirps(start=1, end=float('inf')): # generator for emirps in start..end
    p = nextprime(start-1)
    while p <= end:
        s = str(p)
        if s[0] in "24568":
            p = nextprime((int(s[0])+1)*10**(len(s)-1)); continue
        revp = int(s[::-1])
        if p != revp and isprime(revp): yield p
        p = nextprime(p)
print(list(emirps(end=1201))) # _Michael S. Branicky_, Jan 24 2021, updated Jul 28 2022