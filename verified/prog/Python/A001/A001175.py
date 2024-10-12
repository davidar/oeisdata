from functools import reduce
from sympy import factorint, lcm
def A001175(n):
    if n == 1:
        return 1
    f = factorint(n)
    if len(f) > 1:
        return reduce(lcm, (A001175(a**f[a]) for a in f))
    else:
        k,x = 1, [1,1]
        while x != [0,1]:
            k += 1
            x = [x[1], (x[0]+x[1]) % n]
        return k # _Chai Wah Wu_, Jul 17 2019
print([A001175(n) for n in range(1,31)])
