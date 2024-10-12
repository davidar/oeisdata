from math import sqrt, floor
def A007237(n):
    ct = 0; k = 4*n*n
    for x in range(1, floor(2*sqrt(3)*n) + 1):
        for y in range(max(k//x + 1, x), floor((k+2*n*sqrt(k+x*x))/x)+1):
            if k*(x + y)%(x*y - k) == 0: ct += 1
    return ct  # _Ya-Ping Lu_, Dec 24 2023
print([A007237(n) for n in range(1,31)])
