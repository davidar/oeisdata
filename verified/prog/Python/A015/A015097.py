l=[1]
for n in range(1, 21):
    l.append(sum([(-2)**i*l[i]*l[n - 1 - i] for i in range(n)]))
print(l) # _Indranil Ghosh_, Aug 14 2017