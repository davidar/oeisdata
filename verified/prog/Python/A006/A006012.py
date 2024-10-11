l = [1, 2]
for n in range(2, 101): l.append(4 * l[n - 1] - 2 * l[n - 2])
print(l)  # _Indranil Ghosh_, Jul 02 2017