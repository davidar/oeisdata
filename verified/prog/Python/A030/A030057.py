from sympy import divisors
def A030057(n):
    c = {0}
    for d in divisors(n,generator=True):
        c |=  {a+d for a in c}
    k = 1
    while k in c:
        k += 1
    return k # _Chai Wah Wu_, Jul 05 2023
print([A030057(n) for n in range(1,31)])
