from itertools import islice
def A006279_gen(): # generator of terms
    a, b = 1, 1
    yield a
    while True:
        yield b
        a, b = b, a*(a*b+1)
A006279_list = list(islice(A006279_gen(),10)) # _Chai Wah Wu_, Mar 19 2024
print(A006279_list)
