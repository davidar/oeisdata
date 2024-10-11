from itertools import islice
from sympy import isprime
def A005478_gen(): # generator of terms
    a, b = 1, 1
    while True:
        if isprime(b):
            yield b
        a, b = b, a+b
A005478_list = list(islice(A005478_gen(),10)) # _Chai Wah Wu_, Jun 25 2024
print(A005478_list)
