from sympy import nextprime
def A030665(n):
    d, nd = 10, 10*n
    while True:
        x = nextprime(nd)
        if x < nd+d:
            return int(x)
        d *= 10
        nd *= 10 # _Chai Wah Wu_, May 24 2016
print([A030665(n) for n in range(1,31)])
