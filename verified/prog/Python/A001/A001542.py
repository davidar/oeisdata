l=[0, 2]
for n in range(2, 51): l+=[6*l[n - 1] - l[n - 2], ]
print(l) # _Indranil Ghosh_, Jun 06 2017