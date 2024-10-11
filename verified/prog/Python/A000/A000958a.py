from itertools import accumulate
def A000958_list(size):
    if size < 1: return []
    L, accu = [], [1]
    for n in range(size-1):
        accu = list(accumulate(accu+[-accu[-1]]))
        L.append(accu[n])
    return L
print(A000958_list(29)) # _Peter Luschny_, Apr 25 2016