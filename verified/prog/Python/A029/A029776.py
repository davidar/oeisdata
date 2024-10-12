from itertools import count, islice
def A029776_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:set(str(n)) <= set(str(n**3)), count(max(startvalue,0)))
A029776_list = list(islice(A029776_gen(),20)) # _Chai Wah Wu_, Apr 03 2023
print(A029776_list)
