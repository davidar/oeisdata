l = [0, 1]
for n in range(2, 51):
    x = str(l[n - 1])
    l.append(int(''.join(sorted(str(int(x) + int(x[::-1]))))))
print(l[1:]) # _Indranil Ghosh_, Jul 05 2017