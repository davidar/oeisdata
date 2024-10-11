from itertools import count, islice
def val(n, p):
    e = 0
    while n%p == 0: n //= p; e += 1
    return e
def agen(): # generator of terms
    fi, nz, z = 1, 0, 0
    for i in count(1):
        fi *= 2**val(i, 2) * 5**val(i, 5)
        z = val(fi, 10)
        for k in range(nz+1, nz+z): yield k
        nz += z
        fi //= 10**z
print(list(islice(agen(), 56))) # _Michael S. Branicky_, Apr 13 2022