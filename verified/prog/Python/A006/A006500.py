def a(n, adict={0:1, 1:2, 2:4, 3:8, 4:12, 5:18, 6:27, 7:45}):
    if n in adict:
        return adict[n]
    adict[n]=a(n-1)+a(n-2)-a(n-3)+a(n-4)+a(n-5)+a(n-6)-a(n-7)-a(n-8)
    return adict[n] # _David Nacin_, Mar 07 2012
print([a(n) for n in range(30)])
