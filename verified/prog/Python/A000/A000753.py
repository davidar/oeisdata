from itertools import accumulate, count, islice
def A000753_gen(): # generator of terms
    blist, c = tuple(), 1
    for i in count(0):
        yield (blist := tuple(accumulate(reversed(blist),initial=c)))[-1]
        c = c*(4*i+2)//(i+2)
A000753_list = list(islice(A000753_gen(),30)) # _Chai Wah Wu_, Jun 11 2022
print(A000753_list)
