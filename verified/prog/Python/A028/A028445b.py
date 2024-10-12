# faster, but > memory, version for initial segment of sequence
def icf(s): # incrementally cubefree
    for l in range(1, len(s)//3 + 1):
        if s[-3*l:-2*l] == s[-2*l:-l] == s[-l:]: return False
    return True
def aupton(nn, verbose=False):
    alst, cfs = [1], set("0")
    for n in range(1, nn+1):
        an = 2*len(cfs)
        cfsnew = set(c+i for c in cfs for i in "01" if icf(c+i))
        alst, cfs = alst+[an], cfsnew
        if verbose: print(n, an)
    return alst
print(aupton(30)) # _Michael S. Branicky_, Mar 13 2022