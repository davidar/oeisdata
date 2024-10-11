l=[2]
for n in range(1, 101):
    l.append(l[n - 1] + ((n + 1)//2) if n%2 else l[n - 1]*(n//2))
print(l) # _Indranil Ghosh_, Jul 05 2017