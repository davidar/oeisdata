def a(n):
    if n==1: return 0
    x=0
    while True:
        if not n%2:
            n//=2
            x+=1
        else: n = 3*n + 1
        if n<2: break
    return x
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Apr 14 2017