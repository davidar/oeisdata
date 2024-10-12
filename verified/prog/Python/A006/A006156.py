def isf(s): # incrementally squarefree (check factors ending in last letter)
    for l in range(1, len(s)//2 + 1):
        if s[-2*l:-l] == s[-l:]: return False
    return True
def aupton(nn, verbose=False):
    alst, sfs = [1], set("0")
    for n in range(1, nn+1):
        an = 3*len(sfs)
        sfsnew = set(s+i for s in sfs for i in "012" if isf(s+i))
        alst, sfs = alst+[an], sfsnew
        if verbose: print(n, an)
    return alst
print(aupton(40)) # _Michael S. Branicky_, Jul 21 2021