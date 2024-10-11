A002293_list, x = [1], 1
for n in range(100):
    x = x*4*(4*n+3)*(4*n+2)*(4*n+1)//((3*n+2)*(3*n+3)*(3*n+4))
    A002293_list.append(x) # _Chai Wah Wu_, Feb 19 2016
print(A002293_list)
