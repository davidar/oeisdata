from itertools import count, islice
def A030302_gen(): # generator of terms
    return (int(d) for n in count(1) for d in bin(n)[2:])
A030302_list = list(islice(A030302_gen(),30)) # _Chai Wah Wu_, Feb 18 2022
print(A030302_list)
