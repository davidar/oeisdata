from itertools import count, islice
def A030190_gen(): return (int(d) for m in count(0) for d in bin(m)[2:])
A030190_list = list(islice(A030190_gen(),30)) # _Chai Wah Wu_, Jan 07 2022
print(A030190_list)
