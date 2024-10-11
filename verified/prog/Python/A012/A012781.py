def a(n, adict={0:0, 1:1, 2:4}):
    if n in adict:
        return adict[n]
    adict[n]=5*a(n-1) - 4*a(n-2) + a(n-3)
    return adict[n] # _David Nacin_, Feb 27 2012
print([a(n) for n in range(30)])
