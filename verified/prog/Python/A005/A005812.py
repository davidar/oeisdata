def a(n):
    s=0
    x=0
    while n>0:
        x=n%3
        n//=3
        if x==2:
            x=-1
            n+=1
        if x!=0: s+=1
    return s
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 07 2017