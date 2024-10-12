from itertools import islice
def A028948_gen(): # generator of terms
    x = 0
    while True:
        yield x
        x = (y:=(x*4001+1200)//1000)>>(~y&y-1).bit_length()
A028948_list = list(islice(A028948_gen(),30)) # _Chai Wah Wu_, Dec 28 2023
print(A028948_list)
