l=[0, 3]
for n in range(2, 101):
    l.append(l[n - 1] + (l[n - 1] - 1)//2)
print(l[1:]) # _Indranil Ghosh_, Jun 09 2017