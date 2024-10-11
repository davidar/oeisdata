from sympy import nextprime
from itertools import islice
def agen(): # generator of terms
    pn, an, aset = 2, 1, {1}
    while True:
        yield an
        an = m if (m:=an-pn) > 0 and m not in aset else p if (p:=an+pn) not in aset else 0
        aset.add(an)
        pn = nextprime(pn)
print(list(islice(agen(), 131))) # _Michael S. Branicky_, Mar 07 2024