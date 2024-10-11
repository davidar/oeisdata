from itertools import count, islice
def A003607_gen(): # generator of terms
    return (i for i, s in enumerate(d for n in count(0) for d in bin(n)[2:]) if s == '0')
A003607_list = list(islice(A003607_gen(),30)) # _Chai Wah Wu_, Feb 18 2022
print(A003607_list)
