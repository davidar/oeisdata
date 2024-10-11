def a(n, adict={0:0, 1:1}):
    if n in adict:
        return adict[n]
    adict[n]=3*a(n-1) - a(n-2)
    return adict[n] # _David Nacin_, Mar 04 2012
print([a(n) for n in range(30)])
