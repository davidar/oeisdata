l=[2]
n=s=1
y=''
while n<21:
    x=str(l[n - 1]) + ' '
    for i in range(len(x) - 1):
        if x[i]==x[i + 1]: s+=1
        else:
            y+=str(s)+str(x[i])
            s=1
    x=''
    n+=1
    l.append(int(y))
    y=''
    s=1
print(l) # _Indranil Ghosh_, Jul 05 2017