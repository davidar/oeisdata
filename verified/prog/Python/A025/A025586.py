def a(n):
    if n<2: return 1
    l=[n, ]
    while True:
        if n%2==0: n//=2
        else: n = 3*n + 1
        if not n in l:
            l+=[n, ]
            if n<2: break
        else: break
    return max(l)
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 14 2017