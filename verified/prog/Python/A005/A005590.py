l=[0, 1]
for n in range(2, 101):
    l.append(l[n//2] if n%2==0 else l[(n + 1)//2] - l[(n - 1)//2])
print(l) # _Indranil Ghosh_, Jun 28 2017