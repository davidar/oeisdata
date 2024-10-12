from itertools import count, islice
def A029783_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:not set(str(n))&set(str(n**2)),count(max(startvalue,0)))
A029783_list = list(islice(A029783_gen(),30)) # _Chai Wah Wu_, Feb 12 2023
print(A029783_list)
