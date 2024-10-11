def a(n, adict={0:1, 1:1, 2:1, 3:2}):
    if n in adict:
        return adict[n]
    adict[n]=a(n-1)+a(n-3)+a(n-4)
    return adict[n] # _David Nacin_, Mar 07 2012
print([a(n) for n in range(30)])
