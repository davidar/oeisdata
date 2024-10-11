l=[0]
for n in range(1, 101):
    x=l[n - 1] - n
    if x>0 and not x in l: l+=[x, ]
    else: l+=[l[n - 1] + n]
print(l) # _Indranil Ghosh_, Jun 01 2017