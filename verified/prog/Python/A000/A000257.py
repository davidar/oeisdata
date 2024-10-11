a000257 = [1]
for n in range(1, 25): a000257.append((8*n-4)*a000257[-1]//(n+2))
print(a000257) # _Gennady Eremin_, Mar 22 2022