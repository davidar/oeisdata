from itertools import count, islice
def A030303_gen(): # generator of terms
    return (i + 1 for i, s in enumerate(d for n in count(1) for d in bin(n)[2:]) if s == '1')
A030303_list = list(islice(A030303_gen(),30)) # _Chai Wah Wu_, Feb 18 2022
print(A030303_list)
